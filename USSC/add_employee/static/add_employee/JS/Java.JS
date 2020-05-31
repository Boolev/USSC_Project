function myFunction1() {
  document.getElementById("myDropdown1").classList.toggle("show");
}

function filterFunction1() {
  var input2, filter2, ul, li, a, i;
  input2 = document.getElementById("myInput2");
  filter2 = input2.value.toUpperCase();
  div = document.getElementById("myDropdown");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    if (a[i].innerHTML.toUpperCase().indexOf(filter2) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}

  function myFunction2() {
    document.getElementById("myDropdown2").classList.toggle("show");
  }
  
  function filterFunction2() {
    var input2, filter2, ul, li, a, i;
    input2 = document.getElementById("myInput2");
    filter2 = input2.value.toUpperCase();
    div = document.getElementById("myDropdown2");
    a = div.getElementsByTagName("a");
    for (i = 0; i < a.length; i++) {
      if (a[i].innerHTML.toUpperCase().indexOf(filter2) > -1) {
        a[i].style.display = "";
      } else {
        a[i].style.display = "none";
      }
    }
  }



  function myFunction3() 
  {
    document.getElementById("myDropdown3").classList.toggle("show");
  }
  
  function filterFunction2() {
    var input2, filter2, ul, li, a, i;
    input2 = document.getElementById("myInput2");
    filter2 = input2.value.toUpperCase();
    div = document.getElementById("myDropdown3");
    a = div.getElementsByTagName("a");
    for (i = 0; i < a.length; i++) {
      if (a[i].innerHTML.toUpperCase().indexOf(filter2) > -1) {
        a[i].style.display = "";
      } else {
        a[i].style.display = "none";
      }
    }
  }
  
  function Enableddl1(by_type_of_nar)
  {
    var ddl1 = document.getElementById("ddl1");
    ddl1.disabled = chkddl1.checked ? false : true;
    if (!ddl1.disabled)
    {
      ddl1.focus();
    }
  }


  filterSelection("all_violations")
function filterSelection(c) {
  var x, i;
  x = document.getElementsByClassName("info");
  if (c == "all_violations") c = "";
  // Добавить класс "show" (display:block) к отфильтрованным элементам и удалите класс "show" из элементов, которые не выбраны
  for (i = 0; i < x.length; i++) {
    w3RemoveClass(x[i], "show");
    if (x[i].className.indexOf(c) > -1) w3AddClass(x[i], "show");
  }
}// Показать отфильтрованные элементы
function w3AddClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    if (arr1.indexOf(arr2[i]) == -1) {
      element.className += " " + arr2[i];
    }
  }
}

// Скрыть элементы, которые не выбраны
function w3RemoveClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    while (arr1.indexOf(arr2[i]) > -1) {
      arr1.splice(arr1.indexOf(arr2[i]), 1);
    }
  }
  element.className = arr1.join(" ");
}

// Добавить активный класс к текущей кнопке управления (выделите ее)
var btnContainer = document.getElementById("nar0");
var btns = btnContainer.getElementsByClassName("btn");
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}

function myFunction1() {
  document.getElementById("myDropdown4").classList.toggle("show");
}

function filterFunction1() {
  var input2, filter2, ul, li, a, i;
  input2 = document.getElementById("myInput2");
  filter2 = input2.value.toUpperCase();
  div = document.getElementById("myDropdown4");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    if (a[i].innerHTML.toUpperCase().indexOf(filter2) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}

  function myFunction2() {
    document.getElementById("myDropdown5").classList.toggle("show");
  }
  
  function filterFunction2() {
    var input2, filter2, ul, li, a, i;
    input2 = document.getElementById("myInput2");
    filter2 = input2.value.toUpperCase();
    div = document.getElementById("myDropdown5");
    a = div.getElementsByTagName("a");
    for (i = 0; i < a.length; i++) {
      if (a[i].innerHTML.toUpperCase().indexOf(filter2) > -1) {
        a[i].style.display = "";
      } else {
        a[i].style.display = "none";
      }
    }
  }



  function myFunction3() 
  {
    document.getElementById("myDropdown6").classList.toggle("show");
  }
  
  function filterFunction2() {
    var input2, filter2, ul, li, a, i;
    input2 = document.getElementById("myInput2");
    filter2 = input2.value.toUpperCase();
    div = document.getElementById("myDropdown6");
    a = div.getElementsByTagName("a");
    for (i = 0; i < a.length; i++) {
      if (a[i].innerHTML.toUpperCase().indexOf(filter2) > -1) {
        a[i].style.display = "";
      } else {
        a[i].style.display = "none";
      }
    }
  }


