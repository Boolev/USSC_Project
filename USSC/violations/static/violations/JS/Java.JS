function myFunction1() {
    document.getElementById("myDropdown1").classList.toggle("show1");
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
    document.getElementById("myDropdown2").classList.toggle("show2");
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
    document.getElementById("myDropdown3").classList.toggle("show3");
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
