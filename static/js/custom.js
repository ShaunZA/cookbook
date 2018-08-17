// Code for adding extra input fields for ingredients and instructions

var i = 1;
var j = 1;

function addIngredientFunction() {
    var x = document.createElement("input");
    x.setAttribute("type", "text");
    ++i;
    x.setAttribute("name", "ingredient" + i);
    x.setAttribute("placeholder", "Ingredient " + i + ":");
    document.getElementById("ingredients_list").appendChild(x);
}

function addIstructionFunction() {
    var z = document.createElement("textarea");
    z.setAttribute("type", "text");
    z.setAttribute("class", "materialize-textarea");
    ++j;
    z.setAttribute("name", "instruction" + j);
    z.setAttribute("placeholder", "Instruction " + j + ":");
    document.getElementById("instructions_list").appendChild(z);
}

// Code for removing extra input fields for ingredients and instructions

function removeLastIngredient() {
    --i;
    $('#ingredients_list').children().last().remove();
}

function removeLastInstruction() {
    --j;
    $('#instructions_list').children().last().remove();
}

// Hide/Show the minus button in Create Recipe

function hideIngButtonFunction() {
    var c = document.getElementById('ingredients_list').childNodes.length;
    var x = document.getElementById('removeIngButton');
    if (c > 5) {
        x.style.display = "inline-block";
    } else {
        x.style.display = "none";
    }
}

function hideInsButtonFunction() {
    var c = document.getElementById('instructions_list').childNodes.length;
    var x = document.getElementById('removeInsButton');
    if (c > 5) {
        x.style.display = "inline-block";
    } else {
        x.style.display = "none";
    }
}


// Materialize CSS Init Functions

$(document).ready(function(){
    $('.collapsible').collapsible();
    $('.sidenav').sidenav();
    $('select').formSelect();
  });
