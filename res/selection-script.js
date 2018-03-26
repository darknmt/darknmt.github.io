String.prototype.unquoted = function() {
  return this.replace(/(^')|('$)/g, '')
}

var element = document.getElementById('rem:green-riem-surf');
console.log(element)
var content = window.getComputedStyle(
  element, ':after'
).getPropertyValue('content');

element.innerHTML = element.innerHTML + content.unquoted();

console.log(content.unquoted());