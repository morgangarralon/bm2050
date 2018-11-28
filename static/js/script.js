function getScoreColor(element) {
  if(parseInt(element.html()) > 0) {
    element.removeClass('text-danger');
    element.removeClass('text-muted');
    element.addClass('text-success');
  } else if (parseInt(element.html()) < 0) {
    element.removeClass('text-success');
    element.removeClass('text-muted');
    element.addClass('text-danger');
  } else {
    element.removeClass('text-success');
    element.removeClass('text-danger');
    element.addClass('text-muted');
  }
}