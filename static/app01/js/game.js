
function clickIE(){if(document.all)return false;}
function clickNS(e){if(document.layers||(document.getElementById&&!document.all)){
		if(e.which==2||e.which==3)return false;}
}
if(document.layers){document.captureEvents(Event.MOUSEDOWN);document.onmousedown=clickNS;}
		else{document.onmouseup=clickNS;document.oncontextmenu=clickIE;}
		document.oncontextmenu=new Function("return false");
		if(window.innerWidth){rW=window.innerWidth;rH=window.innerHeight;}else{rW=document.documentElement.clientWidth ? document.documentElement.clientWidth : document.body.clientWidth;rH=document.documentElement.clientHeight ? document.documentElement.clientHeight : document.body.clientHeight;}
		if(window.innerWidth<600){var gW=384;var gH=60;}
		else {var gW=768;gH=120;
		}

		var par_level;
		var par_score;
		var par_game;var par_ad2=1;
		var par_ad3=1;
		var par_ad4=1;
		var par_adx2;
		var par_adx3;
		var par_adx4;

		if(window.innerWidth){rW=window.innerWidth;rH=window.innerHeight;}
		else{rW=document.documentElement.clientWidth ? document.documentElement.clientWidth : document.body.clientWidth;rH=document.documentElement.clientHeight ? document.documentElement.clientHeight : document.body.clientHeight ;}

		var ds_urlhiscore="http://www.6m5m.com/";

		function ds_SHS(){return "";}
		function ds_HS(){}

		var dsp="dse.jpg";
		var dsp=new Array("=0",
			"static/app01/img/game/dse.jpg",
			"http://www.6m5m.com/",
			1,
			0,
			0,
			0,
			"",
			"http://www.6m5m.com/",
			1,
			0,
			0,
			1,
			0,
			"http://www.6m5m.com/",
			"/ad1.jpg",
			"_self",
			"udf23hh3r62srayd4",
			0,
			250,
			16,
			1,
			"Loading ...",
			"ffffff",
			"000000",
			"00bfdf",
			0,
			1,
			0,
			"",
			1,
			1);

