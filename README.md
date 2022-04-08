# Adding stadiums to FIFA Manager 14

This tutorial explains how to get the latest custom 3D stadiums to your game.

<h3>Prerequisites:</h3>

<ul>
  <li>FIFA Manager 14</li>
  <li>Latest Python version, download <a href="https://www.python.org/downloads/">here</a></li>
  <li>py7zr library, user guide <a href="https://py7zr.readthedocs.io/en/latest/user_guide.html/">here</a></li>
</ul>

<h3>Steps:</h3>

<ol>
  <li>Install Python's latest version from the link above.</li>
  <li>After installing Python, press <kbd>Win</kbd> + <kbd>X</kbd>, then click Windows Powershell. Type <code>pip install py7zr</code> to install 7z library.</li>
  <li>Download archives from <a href="https://drive.google.com/drive/folders/1-1c1s9XpXO2O71KKP66DVI0YB8lM2L1g?usp=sharing">here</a> by right clicking the date folder (eg. 2022-03-05). Extract the ZIP file to anywhere you want.</li>
  <li>In this repository, click Code, then click Download ZIP.</li>
  <li>After downloading the ZIP file, navigate to AddStadiumstoFM-main then drag the extracttool.py to where you extracted the archive (eg. inside 2022-03-05)</li>
  <li>Open the archive and you should see country names and National Teams as folders.</li>
  <li>Press <kbd>LShift</kbd> while right click, then click Open PowerShell window here option</li>
  <li>Type <code>python extracttool.py</code> then press <kbd>Enter</kbd></li>
  <li>You will be asked to locate the FULL PATH where you installed the game, this is by default <code>C:\Program Files (x86)\Origin Games\FIFA Manager 14\</code></li>
  <li>Press <kbd>Enter</kbd>, then the script will start adding stadiums</li>
</ol>

<h3>Optional:</h3>
<ul><li>You can use <b>extracttoolspecific.py</b> if you don't want to extract everything, you can just input a country name and only extract its stadiums.</li></ul>
<h3>Troubleshooting:</h3>

<ol>
  <li><b>Q: </b>I can't do the step 2. It gives an error of <code>The term "pip" is not recognized as the name of a cmdlet, function, script file, or executable program.</code>
    <br></br>
    <b>A: </b>Add Python to PATH variable. <a href="https://www.educative.io/edpresso/how-to-add-python-to-path-variable-in-windows">Here's how.</a>
  </li>
    
</ol>

<h3>Contact:</h3>

<ul>
  <li><b><a href="mailto:muratcansarkalkan@gmail.com">E-mail</a></b>
</ul>
<h3>Extra links that could be useful:</h3>

<ul>
  <li><a href="https://www.youtube.com/watch?v=Kn1HF3oD19c">Tutorial on installing Python</a></li>
</ul>
