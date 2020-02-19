// 打开侧边栏
function openNav() {
  document.getElementById("sidebar").style.width = "400px";
  document.getElementById("content").style.marginLeft = "400px";
  $("#openbtn").toggle();
  $("#closebtn").toggle();
}

/* Set the width of the sidebar to 0 and the left margin of the page content to 0 */
function closeNav() {
  document.getElementById("sidebar").style.width = "0";
  document.getElementById("content").style.marginLeft = "0";
  $("#closebtn").toggle();
  $("#openbtn").toggle();
}


//set the labelText function to P1
document.getElementById('P1').addEventListener("mouseup", labelText);
document.getElementById('P1').style.borderLeft = "thick solid #C4D037";//格式

//num and text are for highlight, num calculate the number of highlight, text store the highlight text
var num = 0;
var text = [];

//clickNum calculate the num of click on "Next" button
var clickNum = 1;

var sentenceText = document.getElementById('P1').innerText;

//the highlight function
function labelText()
{
  console.log(sentenceText);
	var selection = window.getSelection();
	var range = selection.getRangeAt(0);

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
  }
  
  
  while (!range.toString().endsWith(' ') && !range.toString().endsWith('.')) {
    range.setEnd(n2, range.endOffset + 1);
  }
  range.setEnd(n2, range.endOffset - 1);
  //console.log(range.toString().endsWith(' '));


  //console.log(range.startContainer.wholeText);
  //console.log(range.startContainer.parentElement.nodeName);

  //get the number and the context of selection
  // let {anchorNode, anchorOffset, focusNode, focusOffset} = selection;
  // console.log(anchorOffset);
  // console.log(focusOffset);

	if (range.collapsed == false && range.startOffset != 1 && num < 3 && range.startContainer.parentElement.nodeName == "P") {
		var node = document.createElement("span");
		node.style.backgroundColor = 'yellow';
    var labelId = clickNum.toString() + num.toString();
    node.setAttribute("id", labelId);
    //console.log(node);
		num += 1;
		range.surroundContents(node);
		console.log(sentenceText.indexOf(node.innerText));
    console.log(sentenceText.indexOf(node.innerText) + node.innerText.length);

    text.push(node.innerText);
    var d = document.getElementById('inputcard');
    var input = document.createElement("textarea");
    input.setAttribute('id', 'questionAsked');
    input.setAttribute('name', 'questionAsked');
    var questiontext = document.createElement("p");
    questiontext.innerText = "What is your question of the sentence?";
    d.appendChild(questiontext);
    d.appendChild(input);

	}
	
}

function vagueConfirm(){
  $("#chooseYes").toggle();
  $("#chooseQuestion").toggle();
}

function vagueDecline(){
  $("#chooseNo").toggle();
  $("#chooseQuestion").toggle();
}

	var curfontsize = 12; 

	
	function zoomin(){
		if (curfontsize < 28){
		curfontsize = curfontsize + 1;
		document.getElementById('P1').style.fontSize = curfontsize +'pt';		
		}
	}
	
	
	function zoomout(){
		if(curfontsize > 10) {
			curfontsize=curfontsize-1;
			document.getElementById('P1').style.fontSize = curfontsize +'pt';
		}
	}


function undo(){
  if(num >= 0){
    num = num - 1;
    var labelId = clickNum.toString() + num.toString();
    last = document.getElementById(labelId);
    last.insertAdjacentText("afterend", text[text.length - 1]);
  
    text.pop();
    last.parentNode.removeChild(last);

    var d = document.getElementById('inputcard');
    d.removeChild(d.childNodes[1]);
    d.removeChild(d.childNodes[0]);
    

  }
}

function clearAll(){
  for(var j = num - 1; j >= 0; j--){
    var labelId = clickNum.toString() + j.toString();
    last = document.getElementById(labelId);
    
    last.insertAdjacentText("afterend", text[text.length - 1]);
  
    text.pop();
    last.parentNode.removeChild(last);
    var d = document.getElementById('inputcard');
    d.removeChild(d.childNodes[1]);
    d.removeChild(d.childNodes[0]);
    

  }
  num = 0;
}


//var clickNum = 1;
function show(){
  console.log(clickNum);
  if (clickNum < 5) {

  
    //remove the function labeText of the previous sentence
    var pID = 'P' + clickNum.toString();
    document.getElementById(pID).removeEventListener("mouseup", labelText);

    //get the value from the textarea and store it to paragraph, and then display it
    q = document.getElementById('questionAsked').value;
    var questionTextID = 'nextPageQuestion' + clickNum.toString();
    document.getElementById(questionTextID).innerText = "Your question is " + "\n" + q;
    var questionID = '#yourQ' + clickNum.toString();
    $(questionID).toggle();

    clearAll();

    text = [];
    num = 0;

    //clear the value of the textarea
    //document.getElementById('questionAsked').value = '';
    document.getElementById(pID).style.border = "none";
    // document.getElementById(pID).style.backgroundColor ="#FFFFFF";

    clickNum += 1;

    //set the function labelText of the next sentence, and then display it
    pID = 'P' + clickNum.toString();
    document.getElementById(pID).addEventListener("mouseup", labelText);

    ppID = 'PP' + clickNum.toString();
    sentenceText = document.getElementById(ppID).innerText;
    var paragraphID = '#P' + clickNum.toString();
    $(paragraphID).toggle();
    document.getElementById(pID).style.borderLeft = "thick solid #C4D037";
    // document.getElementById(pID).style.backgroundColor = "#F8F8F8";

  }else if (clickNum == 5) {
    q = document.getElementById('questionAsked').value;
    var questionTextID = 'nextPageQuestion' + clickNum.toString();
    document.getElementById(questionTextID).innerText = "Your question is " + q;
    var questionID = '#yourQ' + clickNum.toString();
    $(questionID).toggle();

    pID = 'P' + clickNum.toString();
    document.getElementById(pID).removeEventListener("mouseup", labelText);
    document.getElementById(pID).style.border = "none";
    // document.getElementById(pID).style.backgroundColor = "#FFFFFF";

    $('#task1').toggle();
    // $('#wq1').toggle();
    // $('#wq2').toggle();
    // $('#wq3').toggle();
    // $('#wq4').toggle();
    // $('#wq5').toggle();
    $('#s').toggle();
  }

}


