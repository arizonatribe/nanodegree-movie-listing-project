# Movie/TV Trailer Webpage
This simple project demonstrates the use of Python, HTML, JavaScript, and CSS to
view a catalog of Movie and TV titles. 

### The Code Flow
We start with a raw source of media information in a JSON file. Each movie/TV
title is listed in an array inside the `media.json` file. Additional details
for each Movie or TV Show (including synopsis and various multimedia URLs) also
may be found with each title. 

The Python scripts serve the purpose of parsing the JSON raw data into instances
of structured classes and generating dynamic markup from all the valid data it
finds. The `video.py` contains the base class for these multimedia and holds
properties that are common between both `Movie` and `TvShow` classes. Naturally,
the `tv.py` and `movie.py` scripts contain additional details specific to each
class that inherits from the base `Video` class.

The `import_media.py` is the starting point for the project. It imports the
raw JSON data, parses it into different media instances (`Movie`, and `TvShow`),
and then sends that collection of objects into the `create_site.py` script to
be used in generating dynamic HTML markup from each class instance. The
`create_site.py` script generates the actual HTML file, copies the `script.js`
(which is custom jQuery/JavaScript to support the UI) and the `styles.css` all
together into a `public/` directory as the final, publically-viewable product.

### Project dependencies

#### Python
To run this project, you will need to have Python installed, which can be
downloaded [here](https://www.python.org/downloads/). You may in fact,
already have Python installed, which you can verify by opening your command
prompt and typing:

```
python --version
```

or even just:

```
python
```

If you indeed _do_ have Python installed, you'll see either the numeric version
of Python shown to you or some double-caret prompt awaiting you to type in
Python commands.

#### Node (optional)
Additionally, you may find it useful to install [NodeJS](https://nodejs.org/)
to help testing simple, locally-hosted web servers. Of course, there are other
options for locally-hosting your own server. On Windows this can be done with
[IIS-Express](http://www.iis.net/learn/extensions/introduction-to-iis-express).
If you do install Node, you can use Node's package manager (called `npm`) to
install useful 3rd-party tools from the command line. One such recommended tools
is simply called [`serve`](https://www.npmjs.com/package/serve).

To install `serve` (after having already installed NodeJS), open the command
prompt and type:

```
npm install -g serve
```

This will globally install this tool. Now it is very simple to locally host a
webpage. From the command line, navigate to the directory containing the HTML
file(s) you want to test and then just type `serve` to launch a simple NodeJS
server. By default, this will run it on port 3000, but you can change that to
another port if you wish, by instead typing `serve -p 9000` (in that case it
would run on port 9000, but you can pick another port number if you wish).

### Running the project
If the dependencies have been installed, you are ready to run the Python script
`import_media.py` and afterwards to locally host and view the webpage it creates
in the project's `public/` directory.

So first, open the command prompt and navigate to the project directory, then
type:

```
python import_media.py
```

As long as no errors occurred, you should now see three files inside the
project's `public/` directory. Now, unless you are using another means to
locally host the webpage (IIS, etc.), from the command line type:

```
serve public
```

Now, open your webbrowser and go to `http://localhost:3000`. By default, the
`npm` tool we're using (called `serve`) uses port 3000 to run a local NodeJS
server.

You should now be able to browse the Movie and TV Show catalog and click on a
given title to view its trailer, go to its IMDB link and view other additional
details about each title.