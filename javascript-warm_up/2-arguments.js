function printArguments(myArgs) {
  if (!myArgs) {
    console.log("No argument");
  }
  if (myArgs.length === 1) {
    console.log("Argument found");
  }
  console.log(myArgs);
}
