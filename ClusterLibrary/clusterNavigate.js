function changeImage(id, newsrc)
{
    document.getElementById(id).src = newsrc;
}

function focusSubalgebra(srcEmbed, srcFocus)
{
    document.getElementById('embeded').src = srcEmbed;
    document.getElementById('focused').src = srcFocus;
}

function updateFocus(a)
{
    const checkboxes = document.querySelectorAll('input[name="vertex"]:checked');
    let values = [];
    let disable = [];
    checkboxes.forEach((checkbox) => {
	values.push(checkbox.value.split('_')[0]);
	disable.push(checkbox.value.split('_')[1].split(' '));
    });
    document.getElementById('embeded').src = 'graph_embeded_' + values.join('_')+'.png';
    document.getElementById('focused').src = 'graph_focused_' + values.join('_')+'.png';
    document.querySelectorAll('input[name="vertex"]').forEach((checkbox) => checkbox.disabled=false);
    disable.flat().forEach((id) => {document.getElementById(id).disabled=true;});
}

function resetFocus()
{
    const checkboxes = document.querySelectorAll('input[name="vertex"]');
    checkboxes.forEach((checkbox) =>
	{
	    checkbox.checked = false;
	    checkbox.disabled= false;
	});
    updateFocus("");
}
