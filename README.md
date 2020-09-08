<html>
  <head>
  </head>
  <body>
    <center><h1>Terrorism-Analysis-with-Insights-using-python</h1></center>
    <h4>
      As we have more information at our fingertips than ever before, the importance of data visualization has never been greater than it is right now.
    </h4>
    <div>
    In this project the data set has approximately 1,90,000 records.As we are usin python the most power library for doing any type of operation on data is pandas, and     dash,plotly for the components of the ui and for webpage.
    </div>
    <h5>visualization of data is done and represented in the below two ways:</h5>
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
      There are seven dropdown and 1 year range slider UI each for filtering the data asper user requirements based on the inputs.
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
        <li>The user should select region before selecting country abnd similary down the path</li>
        <li>Based on the data inputted the data is filtered with the of call backs</li>
      </ul>
    </div>
    <div>
      The World Map Plot has a legend beside it showing the attacktype based on the filters and they are clickable to select any.
    </div>
    <div>
      <b>
        India Specific Map Plot -
      </b> 
      The Region is fixed and set to South Asia and the country is set to India.
      In addition if user wants to apply filters based on Month, Day, State, City, AttackType the user can apply and see the updated results.
    <div>
      <h3>Chart Tool</h3>
      <div>The Chart Tool has world chart tool and India specific chart tool</div>
      <h3>Chart Tool UI:</h3>
      <div>
        <ul>
          <li>Incidents Grouped By- Region(by default)</li>
          <li>Search Box Filter</li>
          <li>Selecting range of years uisng range slider</li>
          <li>Area Chart</li>
        </ul>
      </div>
      <div>
        The dropdown filter which groups incidents based on dropdown value. This is also the legend of the Area Chart.
      </div>
      <div>
        The Search searches for the selected dropdown filter's content, whether it is contained in it or not. If it yields results then they are shown, if not the original legend is shown that has been selected from the dropdown.
      </div>
      <div>
        <b>India Specific Area Chart -</b> has the region and country selected as 'South Asia' and 'India' by default and then the dropdown filter is applied on it.
      </div>
    </div>
    
  </body>
</html>
