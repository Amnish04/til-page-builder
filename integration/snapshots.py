"""Html snapshots to be used in integration testing"""

snapshots = {
    "yattag_html": """<!DOCTYPE html>
<html lang="en-CA">
  <head>
    <meta charset="utf-8" />
    <title># TIL *Yattag*</title>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="stylesheet" href="./themes/theme.css" />
  </head>
  <body>
    <div class="table-of-contents">
      <h2>Table of Contents</h2>
      <ul>
        <li>
          <a href='#c0c44889665a3b0f195fa5235840086df6bc228af11e66ce1730095e30346c10ec177ad242e36dcf9e260bf04059083a3144a2a5ca4bc4bf210348c54fb294bd'>How to install</a>
        </li>
        <li>
          <a href='#d88db7176ecda7988c6391ccb83175d8ad9dfb0cf1ad6ba73700a62680f6e1b2b140b1fbde9e0aac434f30b138d3ab97a7d6bc0f433c41e189a74e9474b919e3'>How to use</a>
        </li>
      </ul>
    </div>
    <h1 id="e0d32c186662be477e574c51ca1f1e5611a06919a26b92c57a8bdae59b69f84394553c07d24bda12765fa38b8a8e73c57b766d4f0dc5e163aefa54f9780c8682">TIL <em>Yattag</em></h1>
    <p>Today I learned how to use <strong>Yattag</strong>, a python library used to generate html markup in an extremely <em>Pythonic</em> way making the entire process seem like a piece of cake.</p>
    <h2 id="c0c44889665a3b0f195fa5235840086df6bc228af11e66ce1730095e30346c10ec177ad242e36dcf9e260bf04059083a3144a2a5ca4bc4bf210348c54fb294bd">How to install</h2>
    <p>As with any other library, just install the package from <strong><em>Pypi</em></strong> - the package distribution library for python.</p>
    <p>pip install yattag</p>
    <p>And voila, you're ready to use it.</p>
    <h2 id="d88db7176ecda7988c6391ccb83175d8ad9dfb0cf1ad6ba73700a62680f6e1b2b140b1fbde9e0aac434f30b138d3ab97a7d6bc0f433c41e189a74e9474b919e3">How to use</h2>
    <p>Here's a simple code <em>snippet</em> that makes use of this library:</p>
    <p>with tag('p'):</p>
    <p>text("some random text")</p>
  </body>
</html>"""
}
