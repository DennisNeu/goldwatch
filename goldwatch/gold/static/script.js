gold_box = document.getElementById('profit');

// The actual value
gold_worth = document.getElementById('gold-worth').innerText;

gold_worth = parseFloat(gold_worth);

console.log(gold_worth);

if (gold_worth <= 0) {
    gold_box.classList.add('negative')
} else {
    gold_box.classList.add('positive')
}