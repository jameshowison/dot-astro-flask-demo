This is a toy website to demonstrate some Day-1 capabilities with Flask.

Requirements : 
All you need to run this demo is `Python3`, `Flask`, `Astropy`, and `Bokeh`. I leave to
your own discretion how you find yourself with these packages, but `conda` and
`pip` are great allies at this time. Here's the `Flask` installation instructions
if you'd like something more thorough : http://flask.pocoo.org/docs/1.0/installation/

Once you have `Flask`, `Astropy`, and `Bokeh` installed you should be able to run 
the website with :
    
    python serve_site.py

This should return an active session in your terminal : 
     
     * Serving Flask app "serve_site" (lazy loading)
     * Environment: production
       WARNING: Do not use the development server in a production environment.
       Use a production WSGI server instead.
     * Debug mode: on
     * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
     * Restarting with fsevents reloader
     * Debugger is active!
     * Debugger PIN: 102-907-216

If you open up http://0.0.0.0:5000/ in a browser you can play with the website. 
(I recommend an incognito window if you plan to edit and run the site multiple
times -- as often former versions of the site are cached and changes won't
update as you expect.)

There are three existing functionalities :

1. The main page : http://0.0.0.0:5000/
This will direct you to a blank page with the time you opened it. 
It will not update as `Flask` (sans `JavaScript` features built within them) only
supports synchronous content. However refreshing the page will change the time.

2. A light curve plotting function : http://0.0.0.0:5000/plot-light-curve/<proposal #>
This accepts either 14873 or 15304 as the proposal number (that's what data I
had lying around) and creates an interactive `Bokeh` plot of the data. This is a
RESTful format -- so you could auto-populate the site with the proposal if it
were real. 

3. A transformation of the light curve : http://0.0.0.0:5000/transform/<proposal #>
This is mostly to demonstrate how you can generate links to new pages with
buttons in templates, but it simply takes the data from the first page and
re-plots it such that the X axis is now in JD instead of MJD. 

These are obviously quite limited -- in hope that you might have fun expanding
upon these functionalities. A great `Flask` tutorial on the basics exists here :
http://flask.pocoo.org/docs/1.0/tutorial/.

Some good ways to expand this site and your knowledge of `Flask` : 

* Add another file that can be read in by the plotting functions. (It can be
  junk data!) 

* Add some formatting into it! Call in bootstrap or roll your own style guide. 

* Write a form to select the proposal! 

* Write a small interactive `JavaScript` function to hide something in the form 
or dynamically render some content. 
