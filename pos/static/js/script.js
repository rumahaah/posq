var product_ids = [];
var total_price = 0;
var record_id = 0;

function addItem(item_id, item_name, qty, item_price) {
  document.getElementById('removelist-' + item_id).style.visibility = 'hidden';

  var tableBody = document.getElementById('summary-table-body');
  var tr = document.createElement('tr');
  tr.setAttribute('class', 'has-text-grey is-size-5 is-size-6-mobile');

  var td_name = document.createElement('td');
  td_name.setAttribute('class', 'is-uppercase');
  td_name.innerHTML = item_name;

  var td_price = document.createElement('td');
  td_price.innerHTML = new Intl.NumberFormat('id').format(item_price);

  record_id ++;
  var td_qty = document.createElement('td');
  td_qty.setAttribute('id', "qty-" + record_id);
  td_qty.innerHTML = qty;
  
  window ['change_qty'+record_id] = qty;
  window ['subtotal_price'+record_id] = item_price;

  var td_change_qty = document.createElement('td');
  td_change_qty.setAttribute('class', 'has-text-centered');
  td_change_qty.innerHTML = "<a class='has-text-success fas fa-plus-circle fa-2x' onclick='plus(" + record_id + "," + window ['change_qty'+record_id] + ","+ window ['subtotal_price'+record_id] + ")'></a><a class='has-text-warning fas fa-minus-circle fa-2x' onclick='minus(" + record_id + "," + window ['change_qty'+record_id] + ","+ window ['subtotal_price'+record_id] + ")'></a>";

  var td_subtotal_price = document.createElement('td');
  td_subtotal_price.setAttribute('id', "subtotal-" + record_id);
  td_subtotal_price.setAttribute('class', 'has-text-right');
  td_subtotal_price.innerHTML = new Intl.NumberFormat('id').format(item_price);

  total_price += item_price;

  tr.appendChild(td_name);
  tr.appendChild(td_qty);
  tr.appendChild(td_price);
  tr.appendChild(td_subtotal_price);
  tr.appendChild(td_change_qty);

  tableBody.appendChild(tr);
  showTotal(tableBody);

  product_ids.push([item_id, qty]);
  // console.log(product_ids);
}

function plus(record_id, change_qty, subtotal_price) {
  window ['change_qty'+record_id] += change_qty;
  document.getElementById("qty-" + record_id).innerHTML = window ['change_qty'+record_id];
  total_price -= window ['subtotal_price'+record_id];
  window ['subtotal_price'+record_id] += subtotal_price;
  document.getElementById("subtotal-" + record_id).innerHTML = new Intl.NumberFormat('id').format(window ['subtotal_price'+record_id]);
  total_price += window ['subtotal_price'+record_id];
  showTotal(document.getElementById('summary-table-body'));
  product_ids[record_id-1][1]=window ['change_qty'+record_id];
  // console.log(product_ids);
}

function minus(record_id, change_qty, subtotal_price) {
  window ['change_qty'+record_id] -= change_qty;
  if (window ['change_qty'+record_id] < 1 ) {
    window ['change_qty'+record_id] += change_qty;
    // console.log('dah-nol-qty');
  } else {
    document.getElementById("qty-" + record_id).innerHTML = window ['change_qty'+record_id];
  }

  total_price -= window ['subtotal_price'+record_id];
  window ['subtotal_price'+record_id] -= subtotal_price;
  if (window ['subtotal_price'+record_id] < 1 ) {
    window ['subtotal_price'+record_id] += subtotal_price;
    // console.log('dah-nol-total');
  } else {
    document.getElementById("subtotal-" + record_id).innerHTML = new Intl.NumberFormat('id').format(window ['subtotal_price'+record_id]);
  }
  total_price += window ['subtotal_price'+record_id];
  showTotal(document.getElementById('summary-table-body'));
  product_ids[record_id-1][1]=window ['change_qty'+record_id];
  // console.log(product_ids);
}

function showTotal(tableBody) {
  clearTotal();
  tableBody.appendChild(getTotal());
}

function clearAllItems() {
  var table = document.getElementById('summary-table-body');
  while (table.firstChild) {
    table.removeChild(table.firstChild);
  }

  for (var i = 0; i < product_ids.length; i++) {
    document.getElementById('removelist-' + product_ids[i][0]).style.visibility = 'visible';
    // console.log(product_ids[i][0]);
  }

  product_ids = [];
  total_price = 0;
  record_id = 0;
  document.getElementById("customer_name").value = '';

  table.appendChild(getTotal());
}

function clearTotal() {
  var total_tr = document.getElementById("total-tr");
  if (total_tr !== null) {
    total_tr.parentNode.removeChild(total_tr);
  }
}

function getTotal(){
  var tr_total = document.createElement('tr');
  tr_total.setAttribute('id', 'total-tr')

  var td_total_ln1 = document.createElement('td');
  td_total_ln1.innerHTML = "";
  
  var td_total_ln2 = document.createElement('td');  
  td_total_ln2.innerHTML = "";

  var td_total_display = document.createElement('td');
  td_total_display.setAttribute('class', 'has-text-black-bis is-size-5 has-text-centered is-size-6-mobile');
  td_total_display.setAttribute('colspan', '3');
  td_total_display.innerHTML = "Total";

  var td_total_price = document.createElement('td');
  td_total_price.setAttribute('class', 'has-text-black-bis is-size-5 has-text-right is-size-6-mobile');
  td_total_price.innerHTML = new Intl.NumberFormat('id').format(total_price);

  // tr_total.appendChild(td_total_ln1);
  tr_total.appendChild(td_total_display);
  // tr_total.appendChild(td_total_ln2);
  tr_total.appendChild(td_total_price);

  return tr_total;
}

function postOrder(url,user) {
  if ( document.getElementById("customer_name").value.trim() == '' ) {
    customer_name = 'Customer';
  } else {
    customer_name = document.getElementById("customer_name").value;
  }

  data = {
    'username' : user,
    'customer_name' : customer_name,
    'product_ids' : product_ids,
    'total_price' : total_price,
  };

  let csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0];

  let form = document.createElement('form');
  form.action = url;
  form.method = "POST";

  let inp = document.createElement('input');
  inp.type = 'hidden';
  inp.name = 'data';
  inp.value = JSON.stringify(data);

  form.appendChild(csrftoken);
  form.appendChild(inp);

  document.body.appendChild(form);
  form.submit();
}