<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="shortcut icon" href="../../assets/ico/favicon.ico">

    <title>BigDataMining</title>

    <!-- Bootstrap core CSS -->
    <link href="bootstrap-3.1.1-dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <!-- <link href="jumbotron.css" rel="stylesheet"> -->
    <link href="bootstrap-3.1.1-dist/css/bootstrap.css" rel="stylesheet">
    <script src="http://code.jquery.com/jquery-2.1.0.js"></script>
	<!--<script src="http://code.jquery.com/jquery-1.11.0.min.js"></script>
	<script src="http://code.jquery.com/jquery-migrate-1.2.1.min.js"></script>-->

<script>
	$(document).ready(function() {
		$('#getDataset').click(function() {
			$.get('/get_dataset', function(data) {
				$('#showDatasets').html(data);
			});
		});
	});


</script>
</head>

  <body>

    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" style="font-family:'Palatino Linotype', 'Book Antiqua', Palatino, serif;color:#FFAC59" href="#">Big Data Mining as a Service</a>
        </div>
        
      </div>
    </div>

    <!-- Main jumbotron for a primary marketing message or call to action -->
    <div class="jumbotron">
      <div class="container">
       <h2 style="font-family:'Lucida Sans Unicode', 'Lucida Grande', sans-serif;font-style:normal;cursor:pointer">Welcome to CMPE-295B Project</h2><hr>
       	<p>
		<ul style="font-family:'Courier New', Courier, monospace;font-style:normal;font-size:18px;font-weight:bold;color:#400040">
       	<li>Simply upload your dataset.</li>
	 	<li>Select the columns you want to process.</li>
       	<li>Select the classification algorithm.</li>
        </ul></p>
       	<h3 style="font-family:'Lucida Sans Unicode', 'Lucida Grande', sans-serif;font-weight:bold"> And.. see the wonders..<br>
       	 What do you need? Ah! Just a Web Browser! </h3>
      </div>
    </div>

      <div class="container">
       <center><h2 id="uploadbtn">Upload</h2></center>
	   <script>
    	    $( "#uploadbtn").click(function() {
				$("#upload").fadeToggle("fast","swing",function() {
		  });
		});
		</script>
		</script>
        	
    <div id="upload" style="text-align:center; display:none">
		<form id="form1" enctype="multipart/form-data" method="post" action="/upload/train">
	    <label>Upload Training File</label>
	    <input id="TrainingFile" type="file" name="data" multiple class="btn btn-default" style="margin: 10px 0 10px 420px"/>
	    <input type="text" id="category" name="category" />
        <input type="submit" class="btn btn-primary btn-default" id="btnupload" role="button" value="Upload Your Dataset" style="margin: 10px 0 10px 0px" /> 
		</form>
		<form id="form2" enctype="multipart/form-data" method="post" action="/upload/test">
	    <label>Upload Testing File</label>
	    <input id="TestingFile" type="file" name="data" multiple class="btn btn-default" style="margin: 10px 0 10px 420px"/>   
        <input type="text" id="category" name="category" />
        <input type="submit" class="btn btn-primary btn-default" id="btnupload" role="button" value="Upload Your Dataset" style="margin: 10px 0 10px 0px" /> 
		</form>
	
        <div id="msg"><h1>{{msg}}</h1></div>    
      </div>
      
      </div><hr>
    
<div class="container">
       <center><h2 id="classify">Algorithm</h2></center>
	   <script>
    	    $( "#classify" ).click(function() {
				$("#selclassify").fadeToggle("fast","swing",function() {
		  });
		});
		
		function showDiv(btnId)
		{
			HideDiv();
			if(btnId=='btnTrain')
			{
				$('#resultColumnsTrain').show();
			}
			else if(btnId=='btnRF')
			{
				$('#resultColumnsRF').show();
			}
		}
		
		function HideDiv()
		{
			$('#resultColumnsRF').hide();
			$('#resultColumnsTrain').hide();
		}
        </script>
        
        <div id="selclassify" style="text-align:center;display:none">
        <p>
		<input type="button" id="btnTrain" class="btn btn-primary btn-default" role="button" value="Train Logistics Algorithm" onClick="showDiv('btnTrain');" />
		<input type="button" id="btnRF" class="btn btn-primary btn-default" role="button" value="Random Forest Algorithm" onClick="showDiv('btnRF');" />
		<p>If your dataset is already uploaded. <a href="#" id="getDataset">Click Here</a> to get the list.</p>
        	
			<div class="panel panel-default col-lg-4" style="text-align:center">
				<div class="panel-heading">
					<h3 class="panel-title">Datasets</h3>
				</div>
				<div id="showDatasets" class="panel-body" style="overflow-y: auto; height:400px;">
				</div>
			</div>
				
		<script>
		$('#postColumns').submit(function(){
		
		
		var postData = $(this).serializeArray();
		var formURL = $(this).attr("action");
		
		$.ajax(
		{
			url: formURL,
			type: "POST",
			data: postData,
			success: function(data)
			{
				$('#result').html(data);
			}

		});
		});
		</script>
		
		<div id="resultColumnsTrain" class="panel panel-default col-lg-8" style="text-align:center; height:400px; display:none">
		<div class="panel-heading">
					<h3 class="panel-title">Train Logistics Algorithm</h3>
				</div>
			<div id="showColsTr">
				Get Columns with dataset value -- train logistics
			</div>
			<form class="panel-body" name="postColumns" id="postColumns" action="/run_algorithms/train" method="post">
			<input type="hidden" id="datasetname1" name="datasetname" />
			<label>Predictor</label>
			<input type="text" id="predictor" name="predictor" /><br/>
			<label>Target</label>
			<input type="text" id="target" name="target" /><br/>
			<input type="submit" id="btnTR">
			</form>
		</div>
		
		<div id="resultColumnsRF" class="panel panel-default col-lg-8" style="text-align:center; height:400px; display:none">
		<div class="panel-heading">
					<h3 class="panel-title">Random Forest Algorithm</h3>
				</div>
			<div id="showColsRF">
				Get Columns with dataset value -- random forest
			</div>
			<form id="postColumns" class="panel-body" method="post" action="/run_algorithms/random" class="finalProc">
			<input type="hidden" id="datasetname2" name="datasetname" />
			<label>Predictor</label>
			<input type="text" id="predictor" name="predictor" /><br/>
			<label>Target</label>
			<input type="text" id="target" name="target" /><br/>
			<input type="submit">
			</form>
		</div>
      </div>
      </div><hr>
	  
	  <div class="panel panel-default col-lg-8" style="align:center; height:50px">
			<div class="panel-heading">
				<h3 class="panel-title">Output</h3>
			</div>
			<div class="panel-body" id="result">
			<p></p>
			</div>
	  </div>
	  
      <footer class="navbar-fixed-bottom navbar-inverse">
      <p style="color: #FFFFFF; text-align:center">&copy; Kuntal Shah &nbsp; &nbsp; &nbsp; Meet Mehta &nbsp; &nbsp; &nbsp; Neel Anand<br/></p>
      </footer>
    </div> <!-- /container -->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
	
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    <script src="../bootstrap-3.1.1-dist/js/bootstrap.js"></script>
  </body>
</html>