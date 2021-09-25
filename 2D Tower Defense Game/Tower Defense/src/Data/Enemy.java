package Data;

import org.newdawn.slick.opengl.Texture;

import static Helper.Translator.*;

import java.util.ArrayList;

import static Helper.Clock.*;

public class Enemy implements Entity {
	private int width, height, currentCheckpoint;
	private float speed, x, y, hp, startHp;
	Texture texture, hpBackground, hpForeground, hpBorder;
	private Tile startTile;
	private boolean first = true, alive = true;
	private TileGrid grid;
	private ArrayList<Checkpoint> checkpoints;
	private int[] directions;

	// a constructor for creating enemy entities
	public Enemy(Texture texture, Tile startTile, TileGrid grid, int width, int height, float speed, float hp) {
		this.texture = texture;
		this.hpBackground = QuickLoad("Hp Background");
		this.hpForeground = QuickLoad("Hp Foreground");
		this.hpBorder = QuickLoad("Hp Border");
		this.startTile = startTile;
		this.x = startTile.getX();
		this.y = startTile.getY();
		this.width = width;
		this.height = height;
		this.speed = speed;
		this.hp = hp;
		this.startHp = hp;
		this.grid = grid;
		this.checkpoints = new ArrayList<Checkpoint>();
		this.directions = new int[2];// array of 2 directions in x and y plane
		this.directions[0] = 0;// X direction
		this.directions[1] = 0;// Y direction
		directions = findNextDirection(startTile);
		this.currentCheckpoint = 0;
		populateCheckpointList();
	}

	public void update() {
		if (first)// check if this class is being updated for the first time, if so do nothing
			first = false;
		else {
			if (checkpointReached()) {
				// check for anymore checkpoints before moving on
				if (currentCheckpoint + 1 == checkpoints.size())
					endOfMazeReached();
				else
					currentCheckpoint++;
			} else {
				// if there's no more checkpoints, keep going
				x += Delta() * checkpoints.get(currentCheckpoint).getxDirection() * speed;
				y += Delta() * checkpoints.get(currentCheckpoint).getyDirection() * speed;
			}
		}
	}

	// run when last enemy is reached enemy
	private void endOfMazeReached() {
		Player.modifyLives(-1);
		die();
	}

	private boolean checkpointReached() {
		boolean reached = false;
		Tile t = checkpoints.get(currentCheckpoint).getTile();

		if (x > t.getX() - 2 && x < t.getX() + 2 && y > t.getY() - 2 && y < t.getY() + 2) {// check if enemy has reached
																							// within 2 tiles of the
																							// next checkpoint
			reached = true;
			x = t.getX();
			y = t.getY();
		}
		return reached;
	}

	// Takes the array of checkpoints and add the new checkpoints and directions
	private void populateCheckpointList() {
		checkpoints.add(findNextCheckpoint(startTile, directions = findNextDirection(startTile)));
		int counter = 0;
		boolean cont = true;
		while (cont) {
			int[] currentDirection = findNextDirection(checkpoints.get(counter).getTile());// changes current direction
																							// to a moveable direction
			if (currentDirection[0] == 2 || counter == 20) {// if it can't find anywhere else to go after 20
															// checkpoints, stop looking for checkpoints
				cont = false;
			} else {
				checkpoints.add(findNextCheckpoint(checkpoints.get(counter).getTile(),
						directions = findNextDirection(checkpoints.get(counter).getTile())));// keeps going with the
																								// while loop to keep
																								// looking for the next
																								// checkpoint
			}
			counter++;
		}
	}

	// a method that find the end of the enemy's straight path and makes it a
	// checkpoint to turn
	private Checkpoint findNextCheckpoint(Tile s, int[] dir) {
		Tile Next = null;
		Checkpoint c = null;

		boolean found = false;// boolean to decide if there should be a checkpoint
		int counter = 1; // the counter for the amount of tiles the enemy went through

		while (!found) {// makes the enemy move in a straight line to the end and make a checkpoint at
						// the end of the straight line
			if (s.getXPlace() + dir[0] * counter == grid.getTilesWide()
					|| s.getYPlace() + dir[1] * counter == grid.getTilesHigh() || s.getType() != grid
							.getTile(s.getXPlace() + dir[0] * counter, s.getYPlace() + dir[1] * counter).getType()) {

				found = true;
				counter -= 1;// moves back one because checkpoint should be the tile after the method is
								// triggered
				Next = grid.getTile(s.getXPlace() + dir[0] * counter, s.getYPlace() + dir[1] * counter);// makes the
																										// tile into a
																										// checkpoint
			}
			counter++;
		}

		c = new Checkpoint(Next, dir[0], dir[1]);// the coordinates for the new checkpoint
		return c;
	}

	// finds a new direction for the enemy to move towards when it can't move
	// forward anymore
	private int[] findNextDirection(Tile s) {
		int[] dir = new int[2];
		Tile u = grid.getTile(s.getXPlace(), s.getYPlace() - 1);// to move up
		Tile r = grid.getTile(s.getXPlace() + 1, s.getYPlace());// to move right
		Tile d = grid.getTile(s.getXPlace(), s.getYPlace() + 1);// to move down
		Tile l = grid.getTile(s.getXPlace() - 1, s.getYPlace());// to move left

		if (s.getType() == u.getType() && directions[1] != 1) {// check if you can go up
			dir[0] = 0;
			dir[1] = -1;
		} else if (s.getType() == r.getType() && directions[0] != -1) {// check if you can go right
			dir[0] = 1;
			dir[1] = 0;
		} else if (s.getType() == d.getType() && directions[1] != -1) {// check if you can go down
			dir[0] = 0;
			dir[1] = 1;
		} else if (s.getType() == l.getType() && directions[0] != 1) {// check if you can go left
			dir[0] = -1;
			dir[1] = 0;
		} else {
			dir[0] = 2;
			dir[1] = 2;
		}
		return dir;
	}

	public void damage(int amount) {
		hp -= amount;
		if (hp <= 0) {
			die();
			Player.modifyCash(5);// gives player $5 after a enemy is killed
		}
	}

	private void die() {
		alive = false;
	}

//private boolean pathContinues() {//stops the enemy whenever they come across water or dirt
//	boolean answer = true;
//	Tile myTile = grid.GetTile((int) (x / 64), (int) (y / 64));//the tile the enemy is currently on
//	Tile nextTile = grid.GetTile((int) (x / 64) + 1, (int) (y / 64));
//	
//	if ( myTile.getType() != nextTile.getType())//when the enemy tile is not the same as the next tile, they stop
//		answer = false;
//	return answer;
//}

	// creates the health bar for the enemy
	public void draw() {
		float hpPercentage = hp / startHp;// current hp divides total hp will give the percentage of current hp
		DrawQuadTex(texture, x, y, width, height);
		DrawQuadTex(hpBackground, x, y - 16, width, 8);
		DrawQuadTex(hpForeground, x, y - 16, TILE_SIZE * hpPercentage, 8);// a full hp bar takes up a full tile, so
																			// TILE_SIZE * hpPercentage will give the hp
																			// bar the correct size
		DrawQuadTex(hpBorder, x, y - 16, width, 8);
	}

	public int getWidth() {// setters and getters for referencing in other classes
		return width;
	}

	public void setWidth(int width) {
		this.width = width;
	}

	public int getHeight() {
		return height;
	}

	public void setHeight(int height) {
		this.height = height;
	}

	public float getHp() {
		return hp;
	}

	public void setHp(int hp) {
		this.hp = hp;
	}

	public float getSpeed() {
		return speed;
	}

	public void setSpeed(float speed) {
		this.speed = speed;
	}

	public float getX() {
		return x;
	}

	public void setX(float x) {
		this.x = x;
	}

	public float getY() {
		return y;
	}

	public void setY(float y) {
		this.y = y;
	}

	public Texture getTexture() {
		return texture;
	}

	public void setTexture(Texture texture) {
		this.texture = texture;
	}

	public Tile getStartTile() {
		return startTile;
	}

	public void setStartTile(Tile startTile) {
		this.startTile = startTile;
	}

	public boolean isFirst() {
		return first;
	}

	public void setFirst(boolean first) {
		this.first = first;
	}

	public TileGrid getTileGrid() {
		return grid;
	}

	public boolean isAlive() {
		return alive;
	}
}