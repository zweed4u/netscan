function go(){
	setTimeout(function(){
		window.location.href=window.location.href.slice('0',-1).slice('0',16)+(parseInt(window.location.href.slice('0',-1).split('http://')[1].split('.')[3])+1).toString();
		go();
	}, 1000);
}
go();
