% include('header.tpl')

<div id="profiler-createprofile-container">

  <form method="post" action="/profilepatterns">
    <fieldset>
        <legend>Profile</legend>

        <ul>
          <li>Title :<input type="text" name= "title"/></li>
          <li> Description :<input type="text" name= "description"/></li>
          <li> TYPE :<input type="text" name= "type"/></li>
          <li> DIRECTION :<input type="number" name= "direction"/></li>
          <li> INTERVAL :<input type="number" name= "interval"/></li>
          <li> STOP CHECK :<input type="number" name= "stopcheck"/></li>
          <li> SHALLOW WINDOW :<input type="number" name= "shallowWindow"/></li>
          <li> SHALLOW DEPTH :<input type="number" name= "shallowDepth"/></li>
          <li> DEEP DEPTH :<input type="number" name= "deepDepth"/></li>
          <li> DEEP WINDOW :<input type="number" name= "deepWindow"/></li>
          <li> RAMP TIME :<input type="number" name= "rampTime"/></li>
          <li> MAX TIME :<input type="number" name= "maxTime"/></li>
          <li> BACKTRACK_TIMES  :<input type="number" name= "backtrackTimes"/></li>
          <li> BACKTRACK_COUNT :<input type="number" name= "backtrackCount"/></li>
          <li> STALL TIMEOUT :<input type="number" name= "stallTimeout"/></li>
          <li> CTD_WRAPUP_TIME  :<input type="number" name= "ctdWrapupTime"/></li>
          <li> DPDT :<input type="number" name= "dpdt"/></li>
        </ul>
        
        <input type='submit' value='Submit Form'>
        
    </fieldset>
  </form>
    
</div>

% include('footer.tpl')