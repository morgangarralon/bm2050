function getScoreColor(element) {
  if(parseInt(element.html()) > 0) {
    element.removeClass('btn-danger');
    element.removeClass('btn-light');
    element.addClass('btn-success');
  } else if (parseInt(element.html()) < 0) {
    element.removeClass('btn-success');
    element.removeClass('btn-light');
    element.addClass('btn-danger');
  } else {
    element.removeClass('btn-success');
    element.removeClass('btn-danger');
    element.addClass('btn-light');
  }
}