 $(function() {
   var json, tabsState;
   $('li[id="search-people"], li[id="search-teams"], li[id="search-transfers"]').on('click', function(e) {
     var href, json, parentId, tabsState;
     tabsState = localStorage.getItem("tabs-state");
     json = JSON.parse(tabsState || "{}");
     parentId = $(e.target).parents("ul.nav.nav-pills, ul.nav.nav-tabs").attr("id");
     href = $(e.target).attr('href');
     json[parentId] = href;

     $(".nav.nav-pills li").removeClass("active");
     $(this).addClass("active");

     hideTables();

     return localStorage.setItem("tabs-state", JSON.stringify(json));
   });

 tabsState = localStorage.getItem("tabs-state");
 json = JSON.parse(tabsState || "{}");

 $.each(json, function(containerId, href) {
   $("#" + containerId + " a[href=" + href + "]").tab('show');
   hideTables();
   return $("#" + containerId + " a[href=" + href + "]").tab('show');
 });
});

function hideTables() {
  var navPills = document.getElementsByTagName("li");
  var activeNavPill = 'search-people';
  for (i = 0; i < navPills.length; i++) {
    if (navPills[i].className === 'active') {
      activeNavPill = navPills[i].id;
    }
  }

  var tableToBeShown = 'table-people';
  if (activeNavPill === 'search-people') {
    tableToBeShown = 'table-people';
  } else if (activeNavPill === 'search-teams') {
    tableToBeShown = 'table-teams';
  } else if (activeNavPill === 'search-transfers') {
    tableToBeShown = 'table-transfers';
  }

  var tables = document.getElementsByTagName('table');
  for(var i = 0; i < tables.length; i++) {
    var table = tables[i];
    if(table.className.indexOf(tableToBeShown) == -1) {
      table.style.display = 'none';
    } else {
      table.style.display = 'table';
    }
  }
}