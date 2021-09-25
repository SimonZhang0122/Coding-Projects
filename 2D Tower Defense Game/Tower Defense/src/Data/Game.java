package Data;

import static Helper.Translator.QuickLoad;
import static Helper.Translator.TILE_SIZE;

import org.lwjgl.input.Mouse;

import UI.Button;
import UI.UI;
import UI.UI.Menu;

public class Game {

	private TileGrid grid;
	private Player player;
	private WaveManager waveManager;
	private UI gameUI;
	private Menu towerPickerMenu;

	public Game(TileGrid grid) {// creates a new map, player, waves of enemies and cannon towers
		this.grid = grid;
		waveManager = new WaveManager(
				// creates a wave of enemies including the amount of enemies and other infos
				new Enemy(QuickLoad("Enemy64 texture"), grid.getTile(2, 0), grid, TILE_SIZE, 64, 100, 50), 3, 5);
		player = new Player(grid, waveManager);
		player.setUp();
		setupUI();
	}

	private void setupUI() {
		gameUI = new UI();
//		gameUI.addButton("CannonGun", "CannonGun", 0, 0);
//		gameUI.addButton("CannonIce", "CannonGun2", 64, 0);
//		gameUI.createMenu("TowerPicker", 0, 0);
		gameUI.createMenu("TowerPicker", 0, 0);
		towerPickerMenu = gameUI.getMenu("TowerPicker");
		towerPickerMenu.addButton(new Button("CannonGun", QuickLoad("CannonGun"), 0, 0));
		towerPickerMenu.addButton(new Button("CannonIce", QuickLoad("CannonGun2"), 0, 0));
	}

	private void updateUI() {
		gameUI.draw();

		if (Mouse.next()) {
			boolean mouseClicked = Mouse.isButtonDown(0);
			if (mouseClicked) {
				if (towerPickerMenu.isButtonClicked("CannonGun"))
					player.pickTower(new TowerCannonNor(TowerType.CannonRed, grid.getTile(0, 0),
							waveManager.getCurrentWave().getEnemyList()));
				if (towerPickerMenu.isButtonClicked("CannonIce"))
					player.pickTower(new TowerCannonIce(TowerType.CannonIce, grid.getTile(0, 0),
							waveManager.getCurrentWave().getEnemyList()));
			}
		}
	}

	public void update() {
		grid.draw();
		waveManager.update();
		player.update();
		gameUI.draw();
		updateUI();
	}

}
