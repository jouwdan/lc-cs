// Original language-comparison exercise. Run with Node.js.
const assert = require("node:assert/strict");
let x = 4;
let before = x++;
let after = ++x;
assert.deepEqual([x, before, after], [6, 4, 6]);
assert.equal(3 === "3", false);
assert.equal(3 == "3", true); // Deliberate coercion example from the lesson.
assert.equal("3" + 4, "34");
assert.equal(true && false, false);
console.log("JavaScript operator checks passed");
