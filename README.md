<div align="center">
  <h2>Vilnius School of AI - C class final project - Unit Conversion</h2>
</div>

## Jump to...

  - [Intro](#intro)
  - [How To Run](#HowToRun)
  - [Features](#features)
  - [About SMS](#AboutSms)
  - [Units](#units)
  - [Media](#media)
  - [Changelog](#changelog)

## <a name="Intro"></a>Intro

<p>This is a final project for C class graduation, where user can convert units with ease :)<br>
There are unit categories(mass, time, length and etc) and sub units(kg, g, inch, second).</p>
<p>Unit data weere acquired by web-scraping wikipedia with the helper scripts & manual labor.</p>
<p>You can find the project here - <a href="http://gintautass.pythonanywhere.com/" target="_blank"></a>.</p>

## <a name="HowToRun"></a>How to run
<p>These are the steps that you need to take in order to run this project:</p>
<ul>
  <li>0. Install Visual Studio 2017 or 2019 with python packages.</li>
  <li>1. Download .zip file from this repository & extract it.</li>
  <li>2. Open the project in your extraction directory.</li>
  <li>3. Run: <code>pip install -r requirements.txt</code>.</li>
  <li>4. Run the project via VS Debugger.</li> 
</ul>

## <a name="Features"></a>Features

<ul>
  <li>Flask.</li>
  <li>Currently, there are 6 different unit types.</li>
  <li>Easy to use.</li>
  <li>All main units in one place.</li>
  <li>Currency support.</li>
  <li>SMS support(trial).</li>
  <li>Works offline.</li>
  <li>Some Unit Tests!</li>
</ul>

## <a name="AboutSms"></a>About SMS

<p>I implemented a feature where one can send an SMS message and receive unit conversion via SMS message!</p>
<p>I use Twilio provider's trial version and thus it has limitations, like you can't send SMS messages to not trusted numbers.<br>
  You can see it in action from the demos below.<br><br><b>Structure:</b><code>unit category/unit from/unit to/amount</code><br><b>Example:</b> mass/kilogram/gram/1
</p>

## <a name="Units"></a>Units
<ul>
  <li>Time</li>
  <li>Electric current</li>
  <li>Mass</li>
  <li>Length</li>
  <li>Temperature</li>
  <li>Luminous intensity</li>
  <li>Currencies(USD, EUR and more)</li>
</ul>

## <a name="Media"></a>Media

<a target="_blank" href="https://github.com/GintasS/VSOAI-project/blob/master/media/Base.JPG">
  <img src="https://github.com/GintasS/VSOAI-project/blob/master/media/Base.JPG" height="300" style="max-width:50%;"></img>
</a>
<blockquote>Base window.</blockquote>
<br>
<a target="_blank" href="https://github.com/GintasS/VSOAI-project/blob/master/media/Image2.JPG">
  <img src="https://github.com/GintasS/VSOAI-project/blob/master/media/Image2.JPG" height="200" style="max-width:30%;"></img>
</a>
<blockquote>Conversion from fortnight to hours.</blockquote>
<br>
<a target="_blank" href="https://github.com/GintasS/VSOAI-project/blob/master/media/Image3.JPG">
  <img src="https://github.com/GintasS/VSOAI-project/blob/master/media/Image3.JPG" height="200" style="max-width:60%;"></img>
</a>
<blockquote>Conversion from EUR to RUB.</blockquote>
<br>
<a target="_blank" href="https://github.com/GintasS/VSOAI-project/blob/master/media/Image4.JPG">
  <img src="https://github.com/GintasS/VSOAI-project/blob/master/media/Image4.JPG" height="200" style="max-width:60%;"></img>
</a>
<blockquote>Conversion from mace to gram.</blockquote>
<br>
<a target="_blank" href="https://github.com/GintasS/VSOAI-project/blob/master/media/demo3.gif">
  <img src="https://github.com/GintasS/VSOAI-project/blob/master/media/demo3.gif" height="400" style="max-width:60%;"></img>
</a>
<blockquote>Conversion via SMS: 1 kilogram to grams.</blockquote>
<br>
<a target="_blank" href="https://github.com/GintasS/VSOAI-project/blob/master/media/demo4.gif">
  <img src="https://github.com/GintasS/VSOAI-project/blob/master/media/demo4.gif" height="400" style="max-width:60%;"></img>
</a>
<blockquote>Conversion via SMS: 1 kilometre to metre.</blockquote>
<br>
<a target="_blank" href="https://github.com/GintasS/VSOAI-project/blob/master/media/demo5.gif">
  <img src="https://github.com/GintasS/VSOAI-project/blob/master/media/demo5.gif" height="400" style="max-width:60%;"></img>
</a>
<blockquote>Conversion via SMS: edge cases.</blockquote>

## <a name="Changelog"></a>Changelog

<h3>CHANGELOG 7/7/2019</h3>
<ul>
  <li>Moved project from console application to Flask.</li>
  <li>Added basic interface for selecting categories, units, amounts.</li>  
</ul>

<h3>CHANGELOG 18/7/2019</h3>
<ul>
  <li>Added more unit types.</li>
  <li>Fixed main layout of the MVP.</li>
  <li>Code improvements.</li>
</ul>

<h3>CHANGELOG 26/3/2020</h3>
<ul>
  <li>Fixed grammar mistakes.</li>
</ul>
