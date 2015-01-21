function changePage(){
	var nextpage;
	var url=window.location.search.substring(1);
	var url2=url.split('&');
	for(var i=0;i<url2.length;i++){
		var variable=url2[i].split('=');
		if (variable[0]=='page'){
			if( isNaN(variable[1])){
				nextpage=variable[1]+".html"
			}else{
				nextpage="page"+variable[1]+".html";
			}
			
		}
	}	
	if (!nextpage) nextpage="page0.html"
	$("#page").load(nextpage).hide().slideToggle('slow');
}

function goPage(page){
	var boolPage=false;
	var newURL="";
	var parameter="";
	var URL=window.location.href.split('?');
	
	if (URL[1]){
		for(var i = 0;i<URL.length;i++){
			var parameter=URL[1].split('=');
			if (parameter[0]=="page") parameter[1]="page="+page;
			boolPage=true;
		}
	}
	if (boolPage){
		newURL=URL[0]+parameter;		
	}else{
		newURL=URL[0]+"?page="+page;
	}
	window.history.pushState("","",newURL);
	changePage();
}

$(document).ready(changePage);
