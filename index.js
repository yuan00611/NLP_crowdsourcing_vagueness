//---------------------- set up for AMTurk --------------------------//

var content = turkGetParam('content');
var s1 = turkGetParam('s1');
var s2 = turkGetParam('s2');
var s3 = turkGetParam('s3');
var s4 = turkGetParam('s4');
var s5 = turkGetParam('s5');

//console.log(s1);

// document.getElementById('c').innerHTML = decodeURI(content);
// document.getElementById('P1').innerHTML = decodeURI(s1);
// document.getElementById('PP2').innerHTML = decodeURI(s2);
// document.getElementById('PP3').innerHTML = decodeURI(s3);
// document.getElementById('PP4').innerHTML = decodeURI(s4);
// document.getElementById('PP5').innerHTML = decodeURI(s5);

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
  var novagarea = document.getElementById('noVague');
  if (novagarea.value != "") {
    $("#chooseNo").toggle();
    $("#chooseQuestion").toggle();
    $('#chooseNo').offset({top: position});
  }
  
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
  questionCheckWord = ['What', 'what', 'Where', 'where', 'When', 'when', 'Who', 'who', 'Why', 'why', 'Which', 'which', 'Is', 'is', 'Are', 'are', '?']
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
    alert('You can\'t hightlight too much word!');
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
    questiontext.innerText = "What is your question about " + '\'' + node.innerText + '\'' + "?";
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
  if(num >= 0){
    num = num - 1;
    var labelId = clickNum.toString() + num.toString();
    last = document.getElementById(labelId);
    last.insertAdjacentText("afterend", text[text.length - 1]);
  
    text.pop();
    last.parentNode.removeChild(last);

    textNum.pop();
    textNum.pop();

    var d = document.getElementById('inputcard');
    d.removeChild(d.childNodes[1]);
    d.removeChild(d.childNodes[0]);

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
      allQ = 'Your question for ' + '\''+ text[i] + '\'' + ' is ' + q;
      pQ = "<p>" + allQ + "</p>";
      $(questionID).append(pQ);

      returnQuestion.push(q);
    }
    $(questionID).toggle();

    //q = document.getElementById('questionAsked').value;
    //var questionTextID = 'nextPageQuestion' + clickNum.toString();
    //document.getElementById(questionTextID).innerText = "Your question is " + "\n" + q;
    
    

    var d = document.getElementById('inputcard');
    while (d.childNodes.length != 0) {
      d.removeChild(d.childNodes[0]);
    }
    // for(let i = 0; i <= d.childNodes.length; i++){
      
    // }

    returnText.push(text);
    returnNum.push(textNum);


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

    pID = 'P' + clickNum.toString();
    document.getElementById(pID).removeEventListener("mouseup", labelText);
    document.getElementById(pID).style.border = "none";

    $('#task1').toggle();
    $('#s').toggle();
  }

}

function declineNext(){
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
    //document.getElementById(pID).style.borderLeft = "thick solid #C4D037";
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

var form = document.querySelector("form");
form.onsubmit = function(e){
  e.preventDefault();

  document.getElementById("reportId_text").value = JSON.stringify(returnText);
  document.getElementById("reportId_num").value = JSON.stringify(returnNum);
  document.getElementById("reportId_question").value = JSON.stringify(returnQuestion);

  // console.log(returnText);
  // console.log(returnNum);
  // console.log(returnQuestion);

  form.submit();

}



