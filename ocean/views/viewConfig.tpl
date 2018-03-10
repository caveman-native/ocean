<!DOCTYPE html>
<html>
<header>
      <title>View configuration</title>
      <style>
        body {background-color: powderblue;}
        h1   {color: blue;}
        p    {color: red;}
        ul   { padding-left: 5px;}
        li {
        padding: 3 3 3 3;
}

</style>
</header>    
    
<body>

<body>

% include('mission.tpl')

<h2>Current properties are : </h2>    
    
%from readCfg import readProperties
% configMap = readProperties()
    %    for key, value in configMap.items():
<p> {{key}} :  {{value}}</p>
    %end

<p> <a href="/editConfig">Edit</a>  </p>

</body>
% include('footer.tpl')

</head>
