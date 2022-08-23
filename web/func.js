function doTrans() {
    // change btn style
    var ele = document.getElementById("trans-btn")
    ele.className = "btn btn-dark"
    ele.innerText = "Waiting.."
    // disabled btn
    var att = document.createAttribute("disabled")
    ele.setAttributeNode(att)
    // action
    var fp = document.getElementById("pathLabel").value
    eel.trans_from_py(fp)
}

eel.expose(changeBtn)
function changeBtn() {
    var ele = document.getElementById("trans-btn")
    ele.className = "btn btn-success"
    ele.innerText = "Finished."
}


async function getPath() {
	var fp = await eel.choose_path()()
    document.getElementById("pathLabel").value = fp
}