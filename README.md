<html>
  <head>
  </head>
  <body>
    <center><h1>Terrorism-Analysis-with-Insights-using-python</h1></center>
    <h4>
      As we have more information at our fingertips than ever before, the importance of data visualization has never been greater than it is right now.
    </h4>
    <div>
    In this project the data set has approximately 1,90,000 records.
    As we are using python, the most powerful library for doing any type of operation on data is pandas.
    <br>
    Whereas Dash and plotly are the components of the UI(User Interface) and for webpage.
    </div>
    <h5>Visualization of data is done and represented in the below two ways:</h5>
    <ul>
      <li>
        Map Tool
        <ul>
          <li>World Map Plot</li>
          <li>India Map Plot</li>
        </ul>
      </li>
      <li>
        Chart Tool
        <ul>
          <li>World Area Chart - showing number of incident counts vs every year.</li>
          <li>India Specific Area Chart - showing number of incident counts vs every year.</li>
        </ul>
      </li>
    </ul>
    <h3>1. Map UI</h3>
    <div>
      There are seven dropdown and a year range slider in UI each for filtering the data as per user requirements based on the inputs.
    </div>
    <div>The Dropdown UIs are:
      <ul>
        <li>Month</li>
        <li>Date</li>
        <li>Region</li>
        <li>Country</li>
        <li>Province/State</li>
        <li>City</li>
        <li>Attack-Type</li>
      </ul>
      The range slider is for:
      <ul>
        <li>Year</li>
      </ul>
      There are few restrictions like 
      <ul>
        <li>The user has to select month first and then day.</li>
        <li>The user should select region before selecting country and similary down the path</li>
        <li>Based on the data inputted, the data is filtered with the help of call backs</li>
      </ul>
    </div>
    <div>
      The World Map Plot has a legend beside it, showing the attacktype based on the filters and they are clickable to select any.
    </div>
    <div>
      <b>
        India Specific Map Plot :
      </b> 
          The Region and country are fixed and set to South Asia and India respectively. Rest everything works similarly to the World Map tool.
      <div>
      <h3>Chart Tool</h3>
      <div>The Chart Tool has world chart tool and India specific chart tool</div>
      <h3>2. Chart Tool UI:</h3>
      <div>
        <ul>
          <li>Incidents Grouped By- Region(by default)</li>
          <li>Search Box Filter</li>
          <li>Selecting range of years uisng range slider</li>
          <li>Area Chart</li>
        </ul>
      </div>
      <div>
        The dropdown filter, which groups incidents based on dropdown value, is also the legend of the Area Chart.
      </div>
      <div>
        The search filter works as search for a specfic requirement among all, like a country details or attack type or any.
      </div>
      <div>
        <b>
          India Specific Area Chart :
        </b>
     The Region and country are fixed and set to South Asia and India respectively. Rest everything works similarly to the World Chart tool.
      </div>
    </div>
    <div>
      <h2>Important links</h2>
      <a href="https://docs.google.com/document/d/1kxMa4NRGYYPLh4koqmY2GtdzVaRSWGteuGjO0RTrH7U/edit?usp=sharing">Documentation </a>
      <a href="https://drive.google.com/file/d/1BI8_cjbp0HTZAeIbTx-Xtlh-sk4OgKbY/view?usp=sharing">Working Video with Explanation</a>
    </div>
  </body>
</html>
