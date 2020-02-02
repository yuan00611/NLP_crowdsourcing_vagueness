// 打开侧边栏
function openNav() {
  document.getElementById("sidebar").style.width = "400px";
  document.getElementById("content").style.marginLeft = "400px";
}

/* Set the width of the sidebar to 0 and the left margin of the page content to 0 */
function closeNav() {
  document.getElementById("sidebar").style.width = "0";
  document.getElementById("content").style.marginLeft = "0";
}

//set the labelText function to P1
document.getElementById('P1').addEventListener("mouseup", labelText);


//num and text are for highlight, num calculate the number of highlight, text store the highlight text
var num = 0;
var text = [];

//clickNum calculate the num of click on "Next" button
var clickNum = 1;

//the highlight function
function labelText()
{
	var selection = window.getSelection();
	var range = selection.getRangeAt(0);
  //console.log(range);
  //console.log(range.startContainer.parentElement.nodeName);

  //get the number and the context of selection
  let {anchorNode, anchorOffset, focusNode, focusOffset} = selection;
  console.log(anchorOffset);
  console.log(focusOffset);

	if (range.collapsed == false && range.startOffset != 1 && num < 2 && range.startContainer.parentElement.nodeName == "P") {
		var node = document.createElement("span");
		node.style.backgroundColor = 'yellow';
    var labelId = clickNum.toString() + num.toString();
    node.setAttribute("id", labelId);
    //console.log(node);
		num += 1;
		range.surroundContents(node);
		console.log(node.innerText);

    text.push(node.innerText);

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

  }
}

function clearAll(){
  for(var j = num - 1; j >= 0; j--){
    var labelId = clickNum.toString() + j.toString();
    last = document.getElementById(labelId);
    
    last.insertAdjacentText("afterend", text[text.length - 1]);
  
    text.pop();
    last.parentNode.removeChild(last);

  }
  num = 0;
}


//var clickNum = 1;
function show(){
  if (clickNum < 5) {

    text = [];
    num = 0;

    //remove the function labeText of the previous sentence
    var pID = 'P' + clickNum.toString();
    document.getElementById(pID).removeEventListener("mouseup", labelText);

    //get the value from the textarea and store it to paragraph, and then display it
    q = document.getElementById('questionAsked').value;
    var questionTextID = 'nextPageQuestion' + clickNum.toString();
    document.getElementById(questionTextID).innerText = "Your question is " + q;
    var questionID = '#yourQ' + clickNum.toString();
    $(questionID).toggle();

    //clear the value of the textarea
    document.getElementById('questionAsked').value = '';

    clickNum += 1;

    //set the function labelText of the next sentence, and then display it
    pID = 'P' + clickNum.toString();
    document.getElementById(pID).addEventListener("mouseup", labelText);
    var paragraphID = '#P' + clickNum.toString();
    $(paragraphID).toggle();

  }else if (clickNum == 5) {
    q = document.getElementById('questionAsked').value;
    var questionTextID = 'nextPageQuestion' + clickNum.toString();
    document.getElementById(questionTextID).innerText = "Your question is " + q;
    var questionID = '#yourQ' + clickNum.toString();
    $(questionID).toggle();

    document.getElementById(pID).removeEventListener("mouseup", labelText);

    $('#task1').toggle();
    $('#wq1').toggle();
    $('#wq2').toggle();
    $('#wq3').toggle();
    $('#wq4').toggle();
    $('#wq5').toggle();
    $('#s').toggle();
  }

}


