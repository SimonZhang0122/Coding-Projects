package Data;

public class Checkpoint {// class that makes the enemy moves in different directions if it can't move
							// forward anymore

	private Tile tile;
	private int xDirection, yDirection;

	public Checkpoint(Tile tile, int xDirection, int yDirection) {// constructor for checkpoints
		this.tile = tile;
		this.xDirection = xDirection;
		this.yDirection = yDirection;
	}

	public Tile getTile() {// getters and setters
		return tile;
	}

	public int getxDirection() {
		return xDirection;
	}

	public int getyDirection() {
		return yDirection;
	}

}
