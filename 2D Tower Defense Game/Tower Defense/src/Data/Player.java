package Data;

import org.lwjgl.input.Keyboard;
import org.lwjgl.input.Mouse;

import Helper.Clock;

import static Helper.Translator.*;

import java.util.ArrayList;

public class Player {

	private TileGrid grid;
	private TileType[] types;
	private WaveManager waveManager;
	private ArrayList<Tower> towerList;
	private boolean leftMouseButtonDown, rightMouseButtonDown, holdingTower;
	private Tower tempTower;
	public static int Cash, Lives;

	public Player(TileGrid grid, WaveManager waveManager) {// constructor for player
		this.grid = grid;
		this.types = new TileType[3];
		this.types[0] = TileType.Grass;
		this.types[1] = TileType.Dirt;
		this.types[2] = TileType.Water;
		this.waveManager = waveManager;
		this.towerList = new ArrayList<Tower>();
		this.leftMouseButtonDown = false;
		this.rightMouseButtonDown = false;
		this.holdingTower = false;
		this.tempTower = null;
		Cash = 0;
		Lives = 0;
	}

	public void setUp() {// sets up the lives and money as game starts
		Cash = 60;
		Lives = 10;
	}

	public static boolean modifyCash(int amount) {// changes the amount of money as game goes on
		if (Cash + amount >= 0) {
			Cash += amount;
			System.out.println(Cash);
			return true;
		}
		System.out.println(Cash);
		return false;
	}

	public static void modifyLives(int amount) {// changes amount of lives as game goes on
		Lives += amount;
	}

	public void update() {

		// update holdingTower
		if (holdingTower) {
			tempTower.setX(getMouseTile().getX());
			tempTower.setY(getMouseTile().getY());
			tempTower.draw();
		}

		// update all towers in the game
		for (Tower t : towerList) {
			t.update();
			t.draw();
			t.updateEnemyList(waveManager.getCurrentWave().getEnemyList());
		}

		if (Mouse.isButtonDown(0) && !leftMouseButtonDown) {// Handles mouse inputs
			placeTower();
		}
		if (Mouse.isButtonDown(1) && !rightMouseButtonDown) {// Handles mouse inputs
//			if (modifyCash(-45))
//				towerList.add(new TowerCannonIce(TowerType.CannonIce,
//						grid.getTile(Mouse.getX() / TILE_SIZE, (HEIGHT - Mouse.getY() - 1) / TILE_SIZE),
//						waveManager.getCurrentWave().getEnemyList()));// adds a cannon tower when left click is done
		}

		// stop click actions from performing more than once
		leftMouseButtonDown = Mouse.isButtonDown(0);
		rightMouseButtonDown = Mouse.isButtonDown(1);

		while (Keyboard.next()) {// Handles keybord inputs
			if (Keyboard.getEventKey() == Keyboard.KEY_RIGHT && Keyboard.getEventKeyState()) {// slows down game speed
																								// with left key
				Clock.ChangeMultiplier(0.2f);
			}
			if (Keyboard.getEventKey() == Keyboard.KEY_LEFT && Keyboard.getEventKeyState()) {// speeds up game speed
																								// with right key
				Clock.ChangeMultiplier(-0.2f);
			}
		}
	}

	private void placeTower() {
		if (holdingTower)
			if (modifyCash(-tempTower.getCost()))
				towerList.add(tempTower);// adds a seleceted cannon tower when left click is done
		holdingTower = false;
		tempTower = null;
	}

	public void pickTower(Tower t) {
		tempTower = t;
		holdingTower = true;
	}

	private Tile getMouseTile() {
		return grid.getTile(Mouse.getX() / TILE_SIZE, (HEIGHT - Mouse.getY() - 1) / TILE_SIZE);
	}
}