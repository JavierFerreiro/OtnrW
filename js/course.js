$(document).ready(function() {
	$('a.Favorites_Save') .click (function() {
		var link = $(this).attr('href')
		$('.Favorites_Status').load(link, function() {
			$('.Favorites_Delete').show();
		});
		$(this).hide();
		return false;
});
