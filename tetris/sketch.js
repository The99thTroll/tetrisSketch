const WIDTH = 10;
const HEIGHT = 20;
const T_SIZE = 30;

const colors = {
  "red": [255, 0, 0],
  "blue": [0, 50, 255],
  "green": [0, 190, 0]
};

const blocks = {
  'I-piece': {
    'formation': ['x', 'x', 'x', 'x'],
    'height': 1,
    'width': 4
  }  
};

var grid = [];
var spawnedBlock = false;
var currentBlock = {
  'type': "",
  'position': {
    'x': 0,
    'y': 0
  }
};

function tile(x, y, rgb) {
  fill(rgb[0], rgb[1], rgb[2])
  strokeWeight(T_SIZE/5);
  stroke(255, 255, 255);

  rect(x, y, T_SIZE, T_SIZE);
}

function setup() {
  createCanvas(450, 600);

  //Generate grid
  for(var y = 0; y < HEIGHT; y++){
    var row = [];
    for(var x = 0; x < WIDTH; x++){
      row.push('');
    }
    grid.push(row);
  }
}

function draw() {
  //Draw backdrop
  background(0,0,0);

  //Divider for UI
  strokeWeight(10);
  stroke(255, 255, 255);
  line(300, 0, 300, 800);

  //Iterate to generate tiles
  for(var y = 0; y < HEIGHT; y++){
    for(var x = 0; x < WIDTH; x++){
      if(grid[y][x] != ''){
        tile(x*T_SIZE, y*T_SIZE, colors.red);
      }
    }
  }

  //Spawn a block
  if(spawnedBlock == false){
    spawnedBlock = true;
    currentBlock.type = blocks["I-piece"];
    currentBlock.position.x = 0;
    currentBlock.position.y = 0;

    for(var y = 0; y < grid.length; y++){
      for(var x = 0; x < grid[y].length; x++){
        if(x < currentBlock.type.width
          && y < currentBlock.type.height){
          grid[y][x] = 'x';
        }
      }
    }
  }

  //Move a block
  
}