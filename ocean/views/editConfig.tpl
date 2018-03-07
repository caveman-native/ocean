<html>
  <head>
      <title>Update configuration</title>
      <style>
        body {background-color: powderblue;}
        h1   {color: blue;}
        p    {color: red;}
        ul   { padding-left: 5px;}
        li {
        padding: 3 3 3 3;
}

</style>
      
  </head>
  <body>
    <form method="post" action="/">
        
        %from readCfg import readProperties
        % configMap = readProperties()
         <fieldset>
            <legend>Update configiration</legend>
              %  for key, value in configMap.iteritems():
            <ul>
              <li>
                 
                  {{key}}: <input name={{key}} value={{value}} >
                   
              </li>
                  % end            
             </ul>
            <input type='submit' value='Submit Form'>
        </fieldset>
    </form>
    
    <p>{{message}}</p>

  </body>
</html>
   