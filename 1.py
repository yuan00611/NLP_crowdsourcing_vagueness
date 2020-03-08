import boto3
f=open('/u/wjko/NLP_crowdsourcing_vagueness/aws-nodejs-sample/1.tsv','r')
#f2=open('ques.txt','r')
fw=open('hitid.txt','w')
for line in f:
    A=f.readline().split('\t')
    context=A[0]
    if context=='':
        context='-'
    s1=A[1]
    s2=A[2]
    s3=A[3]
    s4=A[4]
    s5=A[5].strip()
    print(A[0]+'@@@')
	#A="""["I would , but I knew that I would be a good man .","Fine , I guess .","I'm not sure . What about you ?","I don't know . I just need to buy a new bedroom .","I'd like to open a Foreign Currency Account .","As long as you bring your ID , etc , we can serve you over the counter . But you won't be able to use the ATM until your new PIN number arrives .","It depends ."]"""
#B="""["I would , but I knew that I would be a good man .","Fine , I guess .","I'm not sure . What about you ?","I don't know . I just need to buy a new bedroom .","I'd like to open a Foreign Currency Account .","As long as you bring your ID , etc , we can serve you over the counter . But you won't be able to use the ATM until your new PIN number arrives .","It depends ."]"""
#C="""["I would , _____ I knew that I would be a good man .","Fine , I guess .","I'm not sure . What about you ?","I don't know . I just need to buy a new bedroom .","I'd like to open a Foreign Currency Account .","As long as you bring your ID , etc , we can serve you over the counter . But you won't be able to use the ATM until your new PIN number arrives .","It depends ."]"""


    que= """
<HTMLQuestion xmlns="http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2011-11-11/HTMLQuestion.xsd">
<HTMLContent>
<![CDATA[
<!DOCTYPE html>
<html>
<head>
	<title>Ask Questions as You Read</title>
	<meta http-equiv='Content-Type' content='text/html; charset=UTF-8'/>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
    <script type='text/javascript' src='https://s3.amazonaws.com/mturk-public/externalHIT_v1.js'></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
   <link href="https://fonts.googleapis.com/css?family=Gochi+Hand|Lato|Montserrat|Open+Sans|PT+Serif|Raleway|Roboto|Source+Sans+Pro|Source+Serif+Pro&display=swap" rel="stylesheet">
    <script src="https://kit.fontawesome.com/532f55454b.js" crossorigin="anonymous"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>
	<style>
	body{
	margin: 0;
}


#sidebar h2{
	padding-top: 30px;
	font-family:'Open Sans', sans-serif;
	font-size: 25pt;
	color: #C4D037;
	margin:0;
}

#sidebar h5{
	padding-left: 12px;
	font-family: 'Open Sans', sans-serif;
}

#sidebar img{
	width: 400px;
	height: auto;
}

#sidebar {
	margin: 0;
	height: 100%; /* 100% Full-height */
	width: 400px;
	background-color: #F2F2F2;
	position: fixed;
	z-index: 1; /* Stay on top */
	overflow: auto;
	text-align: left;
	border-right: 1px solid silver;
	top: 0;
	left: 0;
	overflow-x: hidden; /* Disable horizontal scroll */
	padding-top: 60px; /* Place content 60px from the top */
	padding-left: 10px;
	transition: 0.5s; /* 0.5 second transition effect to slide in the sidebar */
  font-family: 'Roboto', sans-serif;
}


#sidebar .closebtn {
  position: absolute;
  top: 0;
  right: 10px;
  font-size: 36px;
  margin-left: 80px;
  color: #4D4D4D;
}


#moreinfo {
	padding: 10px;
	margin-bottom: 20%;
}

#content {
	height:1000px;
	transition: margin-left .5s; /* If you want a transition effect */
	padding: 20px;
  margin-left: 400px;
}

/*?ìÂ?‰æßËæπ?èÊ???/
#openbtn {
  font-size: 20px;
  cursor: pointer;
  color: gray;
  padding: 10px 15px;
  border: none;
  position: absolute;
  top: 140px;
  right: 10px;
  font-size: 18px;
  margin-left: 500px;
  color: #4D4D4D;
  font-family:'Lato',sans-serif;
}

#openbtn:hover {
  color: #007bff;
}

#closebtn {
  font-size: 20px;
  cursor: pointer;
  color: gray;
  padding: 10px 15px;
  border: none;
  position: absolute;
  top: 140px;
  right: 10px;
  font-size: 18px;
  margin-left: 500px;
  color: #4D4D4D;
  font-family:'Lato',sans-serif;
}

#closebtn:hover {
  color: #007bff;
}

/*#increaseFont {
  font-size: 20px;
  cursor: pointer;
  color: #272727;
  padding: 10px 15px;
  border: none;
  position: absolute;
  top: 15em;
  left: 10px;
  font-size: 1.4em;
  font-family: 'PT+Sefif',serif;
  margin-right: 500px;
  color: #4D4D4D;
}
#increaseFont:hover {
  color: #C4D037
}

#decreaseFont {
  font-size: 20px;
  cursor: pointer;
  color: #272727;
  padding: 10px 15px;
  border: none;
  position: absolute;
  top: 18em;
  left: 10px;
  font-size: 1.4em;
  font-family: 'PT+Sefif',serif;
  margin-right: 500px;
  color: #4D4D4D;
}

#decreaseFont:hover {
color: #C4D037;
}
*/
.page-header {
	background-color: #f0f0f0;
	padding: 20px;
	margin-top: 20px;
	margin-bottom: 30px;
	border-radius: 10px;
}

#context p{
	color: #5e5e5e;
	margin-bottom: 20px;
  letter-spacing: 0.004em;
  line-height: 1.5;
  font-size: 18px;
  font-weight:400;
  font-family: 'Source Serif Pro', serif;
  border-bottom: 0.5px solid silver;
}


#Instruct {
  color:#5e5e5e;
  box-shadow: 0px 0px 0px 0px;
  border: 0.5px solid #DFDFDF;
  padding: 16px;
  width: 30em;
  border-radius: 5px;
  font-size: 18px;
}

#nextPageQuestion1 #nextPageQuestion2{
  font-family:'Lato',sans-serif;
  font-size: 18px;
  letter-spacing: 0.004em;
  line-height: 1.5;
}


.ud {
  background-color: #007bff; 
  color: white;
  border: none;
  border-radius: 3px;
  padding:5px 5px;
  width: 50%;
  margin:3px;
}

.ud:hover {
  background-color: #0069D9;
  cursor: pointer;
}

.ca {
  background-color: #A7A8A9; 
  color: white;
  border-radius: 3px;
  padding:5px 5px;
  width: 50%;
  margin:3px;
}

.ca:hover {
  background-color: #888B8D;
  cursor: pointer;
}

.toolText {
  visibility: hidden;
  width: 120px;
  background-color: black;
  color: #fff;
  text-align: center;
  padding: 5px 0;
  border-radius: 5px;
  font-size: 10pt;
  /* Position the tooltip text - see examples below! */
  position: absolute;
  z-index: 1;
  left:60px;  
}

.ud:hover .toolText {
  visibility: visible;
}
.ca:hover .toolText {
  visibility: visible;
}

.col-md-5 p{
	font-family: 'Source Serif Pro', serif;
  padding: 10px;
  letter-spacing: 0.004em;
  line-height: 1.5;
  font-size: 18px;
  font-weight:400;
  /*cursor: url('https://ionicframework.com/img/finger.png'), auto;*/

	/*border-radius:5px;
	border-right: 1px solid gray;*/
}

.col-md-1 {
  padding:0px;
}
.col-md-6 p{
  font-family: 'Lato', sans-serif;
  font-size: 17px;
  letter-spacing: 0.004em;
  line-height: 1.5;
}   

.card {
  box-shadow: 2px 2px 1px -1px rgba(0, 0, 0, 0.2), 2px 2px 1px -1px rgba(0, 0, 0, 0.14), 2px 2px 1px -1px rgba(0, 0, 0, 0.12);
}       
.card-body{
  margin:0 auto;
}         

.card-body p{
  font-size: 13pt;
}

.btn.btn-secondary {
  background-color: #A7A8A9;
  border: none;
}

.btn.btn-secondary:hover {
  background-color: #888B8D;
  cursor: pointer;
}

.verticalCenter {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: baseline;
}

.buttonControl {
  margin-top: 16px;
  display: flex;
  width: 25rem;
  justify-content: space-around;
  align-items: center;
}

.comment{
	font:bold 15pt "Roboto";
	padding:15px;
}

textarea {
  width: 25rem;
	height: 50px;
	border-radius: .25rem;
	border:1px solid silver;
	font-size: 14pt;
}

.question{
	border:0 none;
	color: #C4D037;
	background-color: white;
}

.question .questiontext {
  visibility: hidden;
  width: 180px;
  background-color: black;
  color: #fff;
  text-align: center;
  padding: 5px 0;
  border-radius: 6px;
  font-size: 10pt;
 
  /* Position the tooltip text - see examples below! */
  position: absolute;
  z-index: 1;
}

.question:hover .questiontext {
  visibility: visible;
}

#task1 {
	/*margin-top: -35%;*/
}

#task1 label {
  margin: 0 auto;
}

#wq2{
	padding-top: 30%;
}

#wq3{
	padding-top: 50%;
}

.confirm{
  background-color: #FFFFFF;
	border:0 none;
	cursor:pointer;
	color: grey;
  margin:auto;
  display: block;
  font-size: 20px;
}

.confirm:hover {
  color: black;
  background-color: white;
}


input[type=submit]{
	padding: 5px 20px;
	background:#C4D037;
	border:0 none;
	cursor:pointer;
	-webkit-border-radius:10px;
	border-radius:5px;
	font:bold 16pt;
	color: white;
	margin-left: 16%;
	margin-top: 20px;
	margin-bottom: 30px;
}
input:hover {
  color: #C4D137;
  border:2px silver;
  background-color: white;
}

#comment{
	text-align: center;
}

@media screen and (max-height: 450px) {
  #sidebar {padding-top: 15px;}
  #sidebar a {font-size: 18px;}
}

	</style>
</head>


<body>

	<div id="sidebar">
		<a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>

		<h2>Instructions</h2>
		<p>Thank you for helping out with our research! Your involvement helps us to advance our understanding of reading comprehension. So before you start, please read the following instructuions carefully.</p>
		<p>We would like to collect <b>high level questions</b> (e.g., questions marked by words like <i>how</i> and <i>why</i>) that occur to you as you read an article. So <b>first</b>, if you see some text in <i>Context</i>, please just read it as this appears before the sentences we ask you to annotate. <b>Then</b>, you will see the next chunk of the article sentence-by-sentence. For each sentence, we'd like to get at <i>where</i> in the sentence that you feel you'd like some <b>elaboration or explanation</b>, and what type of information you're seeking. For example, as you read the sentence</p>
                <p><i><font color="#FF5733">The executive Roland Arnall is well respected in the business world, and by some fair-lending advocates.</font></i></p>
                <p>You might now wonder, <b>why is Roland Arnall well-respected?</b> In this case, the phrase <i>well respected</i> need to be elaborated!</p>
                <p>So the above is our task: we ask you to read a part of an article one sentence at a time, and as you read each sentence:</p>
                <ol>
                  <li>Click "Add Highlight" and highlight the part that you think need elaboration or explanation.</li>
                  <li>Tell us what information you're seeking by <b>asking a question</b> about the part you just highlighted</li>
                  <li>"Add another highlight" if there are more parts of the sentence you want to ask about, or press "Next sentence". You can ask a maximum of 3 questions per sentence.</li>
                </ol>
                <p>Some notes:</p>
                <ul>
                  <li>If the sentence is completely clear to you, a "No Highlight" button will show up after 5 seconds. Use this button only when you're very sure.</li>
                  <li>If you see a green bar showing to the left of the chunk, this means the interface is expecting you to highlight some text.</li>
                  <li>Please, please, write complete questions! We would like to answer them in the end so we need to know what you're really asking for :)</li>
                  <li>Once you move on to the next sentence, you will not be able to edit or delete highlights and questions you did before.</li>
                </ul>
        </div>
        
<form name='mturk_form' method='post' id='mturk_form' action='https://workersandbox.mturk.com/mturk/externalSubmit'>

 <!-- <form name='mturk_form' method='post' id='mturk_form' action='https://www.mturk.com/mturk/externalSubmit'> -->
<input type="hidden" value="" name="assignmentId" id="assignmentId">
<input type="hidden" value="" name="reportId_text" id="reportId_text">
<input type="hidden" value="" name="reportId_num" id="reportId_num">
<input type="hidden" value="" name="eportId_question" id="reportId_question">
<input type="hidden" value="" name="reportId_questionNum" id="reportId_questionNum">


	<div id="content"> <!-- Webpage format control -->
		
		<div class="container">

			<div class="page-header text-center">
				<h1>Ask Questions as You Read</h1>
			</div>

		
		<button id="openbtn" type="button" onclick="openNav()" style="display: none"> << Show instructions</button>
		<button id="closebtn" type="button" onclick="closeNav()">Close instructions>></button>
<!-- 		<button id="increaseFont" type="button" onclick="zoomin()">A+</button>
		<button id="decreaseFont" type="button" onclick="zoomout()">A-</button> -->
		<!-- <div class="alert alert-warning" role="alert">
  This is a warning alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.
</div> -->
			<div class ="row"> <!-- context control-->
				<div class="col-md-5" id="c1">
					<div id="context">
						<h3>Context</h3>
						<p id="c">"""+context+"""</p>
					</div>
				</div>

				<div class="col-1"></div>

			    <!-- <div class="col-md-6"> -->
			    <!-- 	<div id="Instruct" style="width: 30rem;"> -->
			    <!-- 			<p class="card-text">1. Highlight a part of the sentence that you would like elaborated or explained. <br>2. Type a question about the highlighted text in the box appeared later.</p> -->
			    <!-- 	</div> -->
			    <!--     </div> -->

			</div>

	  		<div class="row"> <!-- row 1 -->

	    		<div class="col-md-5" id="PP1">
	      			<p id="P1">"""+s1+"""</p>
				</div>

				<div class="col-1"></div>

			    <div class="col-md-6">
			    	<div>
			    		<div id="yourQ1" style="display: none">
							<p id="nextPageQuestion1"></p>
						</div>
			    	</div>
				</div>
			</div>
			
			<div class="row"><!--Row 2-->
				<div class="col-md-5" id="d2">
					<div id="P2" style="display:none">
	      				<p id = 'PP2'>"""+s2+"""</p>
	      			</div>
	      		</div>
	      		<div class="col-md-1"></div>
	      		<div class="col-md-6">
	      			<div id="yourQ2" style="display: none">
						<p id="nextPageQuestion2"></p>
					</div>	
	      		</div>
	      	</div>
	      	
	      	<div class="row"><!--Row 3-->
	      		<div class="col-md-5" id="d3">
	      			<div id="P3" style="display:none">
	      					<p id = 'PP3'>"""+s3+"""</p>
	      			</div>
	      		</div>
	      		<div class="col-md-1"></div>
	      		<div class="col-md-6">
	      			<div id="yourQ3" style="display: none">
						<p id="nextPageQuestion3"></p>
					</div>
				</div>
	      	</div>

	      	<div class="row"><!--Row 4-->
	      		<div class="col-md-5" id="d4">
	      			<div id="P4" style="display:none">
	      				<p id = 'PP4'>"""+s4+"""</p>
	      			</div>
	      		</div>
	      		<div class="col-md-1"></div>
	      		<div class="col-md-6">
	      			<div id="yourQ4" style="display: none">
						<p id="nextPageQuestion4"></p>
					</div>
				</div>
	      	</div>
	      	
	      	<div class="row"><!--Row 5-->
	      		<div class="col-md-5" id="d5">
	      			<div id="P5" style="display:none">
	      				<p id = 'PP5'>"""+s5+"""</p>
	      			</div>
	      		</div>

	      		<div class="col-md-1"></div>
	      		<div class="col-md-6">
	      			<div id="yourQ5" style="display: none">
						<p id="nextPageQuestion5"></p>
					</div>
	      		</div>
	      	</div>

	      	<div class="row"><!--Row 6-->
	      		<div class="col-md-5"></div>

	      		<div class="col-md-1" id="returnbtn">
	    			<button class="ud" type="button" onclick="undo()">
	    				<i class="fas fa-undo-alt"></i><span class="toolText">Undo your last mark</span>
	    			</button>
	    			<button class="ca" type="button" onclick="clearAll()">
	    				<i class="fas fa-trash-alt"></i><span class="toolText">Clear all your marks</span>
	    			</button>
	    		</div>

	      		<div class="col-md-6">
	      			<div id="task1">
	      			<div id="chooseQuestion">	      				
	      				<div class="card" style="width: 30rem;">
	      					<div class="card-body" >
	      						<div class="buttonControl">
	      						    <button class="btn btn-primary" type="button" onclick="vagueConfirm()">Add Highlight</button> 
	      							<button class="btn btn-primary" type="button" id="no" onclick="vagueDecline()" style="display: none;">No Highlight?</button>
	      						</div>
	      					</div>
	      				</div>
	      			</div>
	      				
	      				<div id="chooseYes" style="display: none">
	      					<div class="card" style="width: 30rem;">
	      						<div class="card-body" >
	      							<div class="verticalCenter">
	      								<p class="card-text">Mark words on the left column</p>
	      								<div id="inputcard"></div>
	      							</div>

	      							<div id="confirmInput" class="buttonControl" style="display: none">
	      								<button type="button" id="confirm" class="btn btn-primary" onclick="inputCheck()">Confirm</button>
	      								<button type="button" id="cancel" class="btn btn-secondary" onclick="undo()">Cancel</button>
	      							</div>

	      							<div id="nextButton" class="buttonControl" style="display: none">
	      								<button type="button" id="anotherH" class="btn btn-primary" onclick="anotherHighlight()" style="display: none">Add another highlight</button>
	      								<button type="button" id="next" class="btn btn-primary" onclick="show()">Next Sentence</button>
	      								
									</div>
								</div>
	      					</div>
	      				</div>

	      				<div id="chooseNo" style="display: none">
	      					<div class="card" style="width: 30rem;">
	      						<div class="card-body" >
	      							<!-- <h5 class="card-title">Instructions</h5> -->
	      							<p>Please type in "I found nothing vague here"</p>
	      							<textarea name="noVague" id="noVague"></textarea>
	      							<button type="button" class="btn btn-primary" onclick="declineNext()">Next</button>
	      						</div>
	      					</div>
	      				</div>
						<br> 
					</div>
				</div>
			</div>

			<div class="row">
				<div class = "col-md-5"></div>
				<div class="col-md-1">
				</div>
				<div class="col-md-6">
					<input type="submit" name="s" value="Submit" id="s" style="display: none;">
				</div>
			</div>
	</div>
</div>
</form>

</body>

<script>
//---------------------- set up for AMTurk --------------------------//

var context =" """+context+""" ";
var s1 = " """+s1+""" ";
var s2 = " """+s2+""" ";
var s3 = " """+s3+""" ";
var s4 = " """+s4+""" ";
var s5 = " """+s5+""" ";

//console.log(s1);

document.getElementById('c').innerHTML = decodeURI(content);
document.getElementById('P1').innerHTML = decodeURI(s1);
document.getElementById('PP2').innerHTML = decodeURI(s2);
document.getElementById('PP3').innerHTML = decodeURI(s3);
document.getElementById('PP4').innerHTML = decodeURI(s4);
document.getElementById('PP5').innerHTML = decodeURI(s5);

turkSetAssignmentID();


//----------------- set up of the starting --------------------------//

//set the labelText function to P1
//document.getElementById('P1').addEventListener("mouseup", labelText);

//position
var position = document.getElementById('PP1').offsetTop;
$('#chooseQuestion').offset({top: position});
$('#returnbtn').offset({top: position});

var position2 = document.getElementById('c1').offsetTop + 50;
$('#Instruct').offset({top: position2});

//left line
document.getElementById("P1").style.borderLeft = "thick solid #C4D037";

//num and text are for highlight, num calculate the number of highlight, text store the highlight text
var num = 0;
var text = [];
var textNum = [];

//for retrieve 
var returnQuesNum = [];
var returnText = [];
var returnNum = [];
var returnQuestion = [];

//clickNum calculate the num of click on "Next" button
var clickNum = 1;

var sentenceText = document.getElementById('P1').innerText;

//no buttom show up
window.setTimeout(showDeclineButton, 10000);

//------------------ sidebar of the instructions ---------------------//
function openNav() {
  document.getElementById("sidebar").style.width = "400px";
  document.getElementById("content").style.marginLeft = "400px";
  $("#openbtn").toggle();
  $("#closebtn").toggle();
}

function closeNav() {
  document.getElementById("sidebar").style.width = "0";
  document.getElementById("content").style.marginLeft = "0";
  $("#closebtn").toggle();
  $("#openbtn").toggle();
}

//-------------------- zoom in / zoom out -------------------------//
// var curfontsize = 18; 

// function zoomin(){
//   if (curfontsize < 25){
//     curfontsize = curfontsize + 1;
//     document.getElementById('content').style.fontSize = curfontsize +'px';   
//   }
// }
  
// function zoomout(){
//   if(curfontsize > 10) {
//     curfontsize=curfontsize-1;
//     document.getElementById('P1').style.fontSize = curfontsize +'px';
//   }
// }

//-------------------- confirm btn func -------------------------//
function showDeclineButton(){
  $("#no").toggle();
}

function vagueConfirm(){
  $("#chooseYes").toggle();
  $("#chooseQuestion").toggle();
  $('#chooseYes').offset({top: position});
  pID = 'P' + clickNum.toString();
  document.getElementById(pID).addEventListener("mouseup", labelText);
  document.getElementById('next').style.display = "none";
  document.getElementById('anotherH').style.display = "none";
}

function vagueDecline(){
  $("#chooseNo").toggle();
  $("#chooseQuestion").toggle();
  $('#chooseNo').offset({top: position});
}


//-------------------- Question Button -------------------------//

function inputCheck(){
  var checked = true;

  AllQues = document.getElementsByClassName('questionAsked');
  for(let i = 0; i < AllQues.length; i++){
    if (AllQues[i].value == "" || AllQues[i].value.length < 10) {
      checked = false;
      //alert("all question should have input");
    }
  }

  var wordCheck = false;
  questionCheckWord = ['What', 'what', 'Where', 'where', 'When', 'when', 'Who', 'who', 'Why', 'why', 'Which', 'which', 'Is', 'is', 'Are', 'are','Do', 'Does', '?']
  for(let i = 0; i < questionCheckWord.length; i++){
    if (AllQues[AllQues.length - 1].value.toString().includes(questionCheckWord[i])) {
      wordCheck = true;      
    }
  }
  if (!wordCheck || !checked) {
    alert("all questions should be a well-structured question!");
  }else if (checked && wordCheck) {
    $('#nextButton').toggle();
    $('#next').toggle();
    document.getElementById('confirmInput').style.display = "none";
    if (num < 3) {
      $('#anotherH').toggle();
    }

  }
      
}

function anotherHighlight(){
  pID = 'P' + clickNum.toString();
  document.getElementById(pID).addEventListener("mouseup", labelText);
  //document.getElementById(pID).style.borderLeft = "thick solid #C4D037";
  document.getElementById('nextButton').style.display = "none";
  document.getElementById('anotherH').style.display = "none";
  document.getElementById('next').style.display = "none";
}





//-------------------- highlight func -------------------------//
function labelText()
{
  console.log(sentenceText);
	var selection = window.getSelection();
	var range = selection.getRangeAt(0);


  //solve the problem of the text --> to be entired
  var o = selection.anchorOffset;
  var n = selection.anchorNode;
  var n2 = selection.focusNode;

  if (o != 0) {
    while (range.toString().indexOf(' ') != 0 && range.startOffset != 0) {  
      range.setStart(n, (range.startOffset - 1));
    }
    if (range.startOffset != 0) {
      range.setStart(n, range.startOffset + 1);
    }
    while (!range.toString().endsWith(' ') && !range.toString().endsWith('.')) {
      range.setEnd(n2, range.endOffset + 1);
    }
    range.setEnd(n2, range.endOffset - 1);
  }
  
  
  //console.log(range.toString().endsWith(' '));


  //console.log(range.startContainer.wholeText);
  //console.log(range.startContainer.parentElement.nodeName);

  //get the number and the context of selection
  // let {anchorNode, anchorOffset, focusNode, focusOffset} = selection;
  // console.log(anchorOffset);
  // console.log(focusOffset);

  if (range.toString().length > 50) {
    alert("You can\'t hightlight too much word!");
  }

	if (range.collapsed == false && num < 3 && range.startContainer.parentElement.nodeName == "P" && range.toString().length < 50) {
		var node = document.createElement("span");
		node.style.backgroundColor = 'rgba(255,204,0,0.6)';
    var labelId = clickNum.toString() + num.toString();
    node.setAttribute("id", labelId);
    //console.log(node);
		num += 1;
		range.surroundContents(node);
		//console.log(sentenceText.indexOf(node.innerText));
    //console.log(sentenceText.indexOf(node.innerText) + node.innerText.length);

    text.push(node.innerText);
    textNum.push(sentenceText.indexOf(node.innerText));
    textNum.push(sentenceText.indexOf(node.innerText) + node.innerText.length);

    $('#confirmInput').toggle();



    var d = document.getElementById('inputcard');
    var input = document.createElement("textarea");
    input.setAttribute('class', 'questionAsked');
    input.setAttribute('name', 'questionAsked');
    var questiontext = document.createElement("p");
    questiontext.innerText = "What is your question about " + "\'" + node.innerText + "\'" + "?";
    d.appendChild(questiontext);
    d.appendChild(input);
    // if (num == 1){
    //   $('#nextButton').toggle();
    // }

    pID = 'P' + clickNum.toString();
    document.getElementById(pID).removeEventListener("mouseup", labelText);
    //document.getElementById(pID).style.border = "none";
    //$('#next').toggle();
    
    
	}
	
}


//-------------------- highlight undo -------------------------//
function undo(){
  anotherHighlight();
  if(num > 0){
    num = num - 1;
    var labelId = clickNum.toString() + num.toString();
    last = document.getElementById(labelId);
    last.insertAdjacentText("afterend", text[text.length - 1]);
  
    text.pop();
    last.parentNode.removeChild(last);

    textNum.pop();
    textNum.pop();

    var d = document.getElementById('inputcard');
    d.removeChild(d.childNodes[d.childNodes.length - 1]);
    d.removeChild(d.childNodes[d.childNodes.length - 1]);

    document.getElementById('confirmInput').style.display = 'none';
    
    if (num == 0) {
      document.getElementById('nextButton').style.display = 'none';
    }
  }
}

//-------------------- highlight clear-------------------------//
function clearAll(){
  anotherHighlight();
  for(var j = num - 1; j >= 0; j--){
    var labelId = clickNum.toString() + j.toString();
    last = document.getElementById(labelId);
    
    last.insertAdjacentText("afterend", text[text.length - 1]);
  
    text.pop();
    last.parentNode.removeChild(last);

    textNum.pop();
    textNum.pop();

    var d = document.getElementById('inputcard');
    d.removeChild(d.childNodes[1]);
    d.removeChild(d.childNodes[0]);
    

  }
  num = 0;
  document.getElementById('nextButton').style.display = 'none';
}




//var clickNum = 1;
function show(){
  //console.log(clickNum);
  if (clickNum < 5) {
  
    //remove the function labeText of the previous sentence
    var pID = 'P' + clickNum.toString();
    document.getElementById(pID).removeEventListener("mouseup", labelText);

    var questionID = '#yourQ' + clickNum.toString();
    //get the value from the textarea and store it to paragraph, and then display it
    AllQues = document.getElementsByClassName('questionAsked');
    for(let i = 0; i < AllQues.length; i++){
      q = AllQues[i].value;
      allQ = "Your question for " + "\'"+ text[i] + "\'" + " is " + q;
      pQ = "<p>" + allQ + "</p>";
      $(questionID).append(pQ);

      returnQuestion.push(q);
    }
    $(questionID).toggle();

    //q = document.getElementById('questionAsked').value;
    //var questionTextID = 'nextPageQuestion' + clickNum.toString();
    
    

    var d = document.getElementById('inputcard');
    while (d.childNodes.length != 0) {
      d.removeChild(d.childNodes[0]);
    }
    // for(let i = 0; i <= d.childNodes.length; i++){
      
    // }

    returnText.push(text);
    returnNum.push(textNum);
    returnQuesNum.push(clickNum);


    text = [];
    textNum = [];
    num = 0;

    document.getElementById('nextButton').style.display = 'none';
    document.getElementById('no').style.display = 'none';
    window.setTimeout(showDeclineButton, 5000);

    //clear the value of the textarea
    // document.getElementById('questionAsked').value = '';
     document.getElementById(pID).style.border = "none";
    // document.getElementById(pID).style.backgroundColor ="#FFFFFF";

    clickNum += 1;

    //set the function labelText of the next sentence, and then display it
    pID = 'P' + clickNum.toString();
    //document.getElementById(pID).addEventListener("mouseup", labelText);

    ppID = 'PP' + clickNum.toString();
    sentenceText = document.getElementById(ppID).innerText;
    var paragraphID = '#P' + clickNum.toString();
    $(paragraphID).toggle();
    document.getElementById(pID).style.borderLeft = "thick solid #C4D037";
    // document.getElementById(pID).style.backgroundColor = "#F8F8F8";

    dID = 'd' + clickNum.toString();
    position = document.getElementById(dID).offsetTop;
    //console.log(position);
    $("#chooseYes").toggle();
    $("#chooseQuestion").toggle();


  }else if (clickNum == 5) {
    var questionID = '#yourQ' + clickNum.toString();
    AllQues = document.getElementsByClassName('questionAsked');
    for(let i = 0; i < AllQues.length; i++){
      q = AllQues[i].value;
      allQ = 'Your question for ' + text[i] + ' is ' + q;
      pQ = "<p>" + allQ + "</p>";
      $(questionID).append(pQ);

      returnQuestion.push(q);
    }
    $(questionID).toggle();
    // q = document.getElementById('questionAsked').value;
    // var questionTextID = 'nextPageQuestion' + clickNum.toString();
    // document.getElementById(questionTextID).innerText = "Your question is " + q;
    // var questionID = '#yourQ' + clickNum.toString();
    // $(questionID).toggle();

    returnText.push(text);
    returnNum.push(textNum);
    returnQuesNum.push(clickNum);

    pID = 'P' + clickNum.toString();
    document.getElementById(pID).removeEventListener("mouseup", labelText);
    document.getElementById(pID).style.border = "none";

    $('#task1').toggle();
    $('#s').toggle();
  }

}

function declineNext(){
  var novagarea = document.getElementById('noVague');
  if (novagarea.value == "I found nothing vague here") {
  if (clickNum < 5) {
  
    //remove the function labeText of the previous sentence
    var pID = 'P' + clickNum.toString();
    document.getElementById(pID).removeEventListener("mouseup", labelText);

    //get the value from the textarea and store it to paragraph, and then display it
    var questionTextID = 'nextPageQuestion' + clickNum.toString();
    document.getElementById(questionTextID).innerText = 'You found nothing vague here.';
    var questionID = '#yourQ' + clickNum.toString();
    $(questionID).toggle();

    document.getElementById('noVague').value = '';

    text = [];
    num = 0;

    document.getElementById('nextButton').style.display = 'none';

    //clear the value of the textarea
    //document.getElementById('questionAsked').value = '';
    document.getElementById(pID).style.border = "none";
    // document.getElementById(pID).style.backgroundColor ="#FFFFFF";
    document.getElementById('no').style.display = 'none';
    window.setTimeout(showDeclineButton, 5000);

    clickNum += 1;

    //set the function labelText of the next sentence, and then display it
    pID = 'P' + clickNum.toString();
    //document.getElementById(pID).addEventListener("mouseup", labelText);

    ppID = 'PP' + clickNum.toString();
    sentenceText = document.getElementById(ppID).innerText;
    var paragraphID = '#P' + clickNum.toString();
    $(paragraphID).toggle();
    document.getElementById(pID).style.borderLeft = "thick solid #C4D037";
    // document.getElementById(pID).style.backgroundColor = "#F8F8F8";

    dID = 'd' + clickNum.toString();
    position = document.getElementById(dID).offsetTop;
    //console.log(position);
    $("#chooseNo").toggle();
    $("#chooseQuestion").toggle();


  }else if (clickNum == 5) {
    var questionTextID = 'nextPageQuestion' + clickNum.toString();
    document.getElementById(questionTextID).innerText = 'You found nothing vague here.';
    var questionID = '#yourQ' + clickNum.toString();
    $(questionID).toggle();

    pID = 'P' + clickNum.toString();
    document.getElementById(pID).removeEventListener("mouseup", labelText);
    document.getElementById(pID).style.border = "none";

    $('#task1').toggle();
    // $('#wq1').toggle();
    // $('#wq2').toggle();
    // $('#wq3').toggle();
    // $('#wq4').toggle();
    // $('#wq5').toggle();
    $('#s').toggle();
  }
}
}

var form = document.querySelector("form");
form.onsubmit = function(e){
  e.preventDefault();

  document.getElementById("reportId_text").value = JSON.stringify(returnText);
  document.getElementById("reportId_num").value = JSON.stringify(returnNum);
  document.getElementById("reportId_question").value = JSON.stringify(returnQuestion);
  document.getElementById("reportId_questionNum").value = JSON.stringify(returnQuesNum);

  // console.log(returnText);
  // console.log(returnNum);
  // console.log(returnQuestion);

  form.submit();

}



</script>
</html>

]]>
</HTMLContent>
<FrameHeight>2000</FrameHeight>
</HTMLQuestion>
"""

    client = boto3.client('mturk',endpoint_url = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com')
#      client = boto3.client('mturk')
    print(client.get_account_balance()['AvailableBalance'])

    response = client.create_hit(
    MaxAssignments=5,
    AutoApprovalDelayInSeconds=797467,
    LifetimeInSeconds=500000,
    AssignmentDurationInSeconds=601,
    Reward='0.05',
    Title='Insert a word to connect to text segments',
    Keywords='sentence,reading',
    Description='This task asks your opinion on how two text segments are connected.',
    Question=que,
    
    RequesterAnnotation='string',
    QualificationRequirements=[
        {
            'QualificationTypeId': '00000000000000000040',
            'Comparator': 'GreaterThan',
            'IntegerValues': [
                -1#500
            ],
            'RequiredToPreview':True
        },
               {
            'QualificationTypeId': '00000000000000000071',
            'Comparator': 'EqualTo',
            'LocaleValues': [
                {
                    'Country': 'US'
                },
            ],
                'RequiredToPreview':True
        },
               {
            'QualificationTypeId': '000000000000000000L0',
            'Comparator': 'GreaterThan',
            'IntegerValues': [
                0#98
            ],
            'RequiredToPreview':True
        }
    ],
#    UniqueRequestToken='14'
)
# The response included several helpful fields
    hit_group_id = response['HIT']['HITGroupId']
    hit_id = response['HIT']['HITId']

# Let's construct a URL to access the HIT
    sb_path = "https://workersandbox.mturk.com/mturk/preview?groupId={}"
    hit_url = sb_path.format(hit_group_id)
    fw.write(hit_id)
    fw.write('\n')
    print(hit_id)
    print(hit_url)