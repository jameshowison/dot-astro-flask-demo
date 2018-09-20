""" This is a quick n dirty flask demo.
The idea is to look at how we can import 
cool Python packages (homegrown or otherwise)
and turn them into cool web content!

Authors
-------
    Jules Fowler, Septemper 2018
"""



## -- IMPORTS
import datetime
import os

from astropy.io import ascii
from astropy.time import Time
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for

## -- SITE SETUP
app = Flask(__name__)


## -- FUNCTIONS

@app.route('/')
def main():
    """ Main function to display the time at which
    the user started up the site."""

    # Create some interesting evolving content
    time = str(datetime.datetime.now())

    # And return it as a template to serve.
    return render_template('time.html', time=time) 


@app.route('/transform/<proposal>')
def transform(proposal):
    """ Transforms the light curve from MJD to JD.

    Parameters
    ----------
    proposal : str
        The proposal to plot.
    """
    # Open the file.
    data_file = './data/{}.csv'.format(proposal)
    data = ascii.read(data_file)
    mjd, flux = data['mjd'], data['flux']
    mjd_transform = Time(mjd, format='mjd').jd
         
    # Plot it up
    TOOLS = 'box_zoom,resize,reset'
    plot = figure(tools=TOOLS, title='Light Curve : Proposal {}'.format(proposal), 
            plot_width=700, plot_height=500)
    plot.circle(mjd_transform, data['flux'], alpha=.2, color='black', size=10)
    
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()
    lc_script, lc_plot = components(plot)
    
    # Pass the plot to a template.
    return render_template('transform.html', 
                  lc_plot=lc_plot, lc_script=lc_script, 
                  js=js_resources, css=css_resources)



@app.route('/plot-light-curve/<proposal>')
def plot_light_curve(proposal):
    """Function to plot a light curve.

    Parameters
    ----------
    proposal : str
        The proposal to plot up.
    """
    
    # Open the file.
    data_file = './data/{}.csv'.format(proposal)
    data = ascii.read(data_file)
    mjd, flux = data['mjd'], data['flux']
         
    # Plot it up
    TOOLS = 'box_zoom,resize,reset'
    plot = figure(tools=TOOLS, title='Light Curve : Proposal {}'.format(proposal), 
            plot_width=700, plot_height=500)
    plot.circle(mjd, data['flux'], alpha=.2, color='black', size=10)
    
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()
    lc_script, lc_plot = components(plot)
    
    # Pass the plot to a template.
    return render_template('plot-light-curve.html', 
                  lc_plot=lc_plot, lc_script=lc_script, 
                  js=js_resources, css=css_resources,
                  prop=proposal)


## -- RUN
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
