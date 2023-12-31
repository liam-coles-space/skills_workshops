# Getting visibility to understand the `this` keyword in JavaScript

## Instructions

At a high level, this week is about building the skills that let you learn a new language and its patterns.  In this workshop, you'll practice getting visibility to understand a language feature: the `this` keyword.

### Learning objectives

1. Describe the `this` keyword as similar to `self` in Ruby.
2. Explain some of the similarities and differences between the behaviour of the `this` keyword and the behaviour of `self` in Ruby.
3. Explain the rules that govern the value of the `this` keyword.

### Getting visibility

A great way to understand code is to get visibility.  One technique for this is to `p` everywhere.   In JavaScript, the equivalent of `p` is `console.log()`. As you go through the workshop, use `console.log()` to see the values of:

* `this`
* Variables
* Parameters
* Function return values

### Questions (30 mins)

* Pair up.

* Clone this repo.

* Open the `index.html` file in your web browser.

* Open the browser console.

* You should see `hello!`.

* Open `index.js` in your text editor.

* Paste the code for question 1 (below) into `index.js`.

* Play around with the code using the techniques for getting visibility. Answer the questions that are in comments.

* Discuss your answers with your pair partner.

* Swap driver and navigator.  Continue with the next question.

### Plenary (15 mins)

We'll come back together for a short plenary to discuss our answers to the questions.

## Questions

Note: the code in many of these questions is not realistic or idiomatic JavaScript.  It's just for illustrating clear examples of the behaviour of the `this` keyword.

### Question 1

```js
function Person() {
  // What is the value of `this` at this point in the program?
  // What other variable in the program has the same value?
};

let person = new Person();
```

### Question 2

```js
function Person() {
  // What is the value of `this` at this point in the program?
  // Maybe research the window object to find out more.
};

// In this version, the programmer has forgotten to put `new` before
// `Person()`
let person = Person();
```

### Pause

Questions 1 and 2 start to explore the effects of the `new` keyword.  But they are only a starting point.  Many things remain a mystery.  Like, what value does `person` get assigned in question 2? Later questions in this workshop will prompt you to explore some of these mysteries.  But many mysteries will remain.

After you complete each question, ask yourself, "What could I change about the code to more fully explore the behaviour I'm seeing?" Make the change to the code, form a hypothesis about what the effect will be, then run the code to see if you're right.  Repeat the process.

### Question 3

```js
function Person() {
  this.count = 5;

  // On what object is the `count` property now stored?
};

// Oh no! Accidentally left out `new` AGAIN!
Person();

// Bonus question: on what object is the `Person` function
// stored?
```

### Question 4

```js
function ClickCount() {
  this.count = 0;

  let self = this;
  $(window).on("click", function() {
    // Why is `self` used here?
    // What would happen if `this` was used instead of `self`?
    self.count++;
  });
};

let clickCount = new ClickCount();
```

### Question 5

```js
function Person() {
  this.name = "Mary";
};

Person.prototype = {
  exclaimName: function() {
    // What is the value of `this` the first time `exclaimName` is run?
    // What about the second time?
    // Research project: Why?

    return this.name + "!";
  }
};

let person = new Person();
console.log(person.exclaimName());

let exclaimName = person.exclaimName;
console.log(exclaimName());
```

### Question 6

```js
function Person() {
  this.name = "Mary";
};

function exclaimName() {
  // What is the value of `this` the first time `exclaimName` is run?
  // What about the second time?
  // Research project: Why?

  return this.name + "!";
};

console.log(exclaimName());

let person = new Person();
person.exclaimName = exclaimName;
console.log(person.exclaimName());
```

### Question 7

```js
// What value does `this` have here?
this;
```

### Question 8

```js
function exclaimName() {
  // What is the value of `this` the first time `exclaimName` is run?
  // What about the second time?
  // What about the third time?
  // Research project: what's the difference between call and apply?

  return this.name + "!";
};

console.log(exclaimName());

let exclaimMary = exclaimName.call({ name: "Mary" });
console.log(exclaimMary);

let exclaimIsla = exclaimName.apply({ name: "Isla" });
console.log(exclaimIsla);
```

### Question 9

Can you list the rules that govern the value of `this`?

## Resources

* [Understand JavaScript's this with clarity](http://javascriptissexy.com/understand-javascripts-this-with-clarity-and-master-it/)
* More examples of the `this` keyword in JavaScript in the [Count project repo](https://github.com/maryrosecook/count)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=javascript_fundamentals/getting_visibility_to_understand_the_this_keyword/README.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=javascript_fundamentals/getting_visibility_to_understand_the_this_keyword/README.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=javascript_fundamentals/getting_visibility_to_understand_the_this_keyword/README.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=javascript_fundamentals/getting_visibility_to_understand_the_this_keyword/README.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=javascript_fundamentals/getting_visibility_to_understand_the_this_keyword/README.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
