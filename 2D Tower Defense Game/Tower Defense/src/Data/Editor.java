package Data;

import static Helper.Translator.HEIGHT;
import static Helper.Translator.TILE_SIZE;

import org.lwjgl.input.Keyboard;
import org.lwjgl.input.Mouse;

import static Helper.Loader.*;

public class Editor {// this creates the menu and functions for the editor screen which you can
						// create your own maps

	private TileGrid grid;
	private int index;
	private TileType[] types;

	public Editor() {
		this.grid = LoadMap("Map");
		this.index = 0;

		this.types = new TileType[3];
		this.types[0] = TileType.Grass;
		this.types[1] = TileType.Dirt;
		this.types[2] = TileType.Water;
	}

	public void update() {
		grid.draw();
		// Handles mouse inputs
		if (Mouse.isButtonDown(0)) {
			setTile();// creates a tile of choice on the map when left click
		}

		// Handles keybord inputs
		while (Keyboard.next()) {
			if (Keyboard.getEventKey() == Keyboard.KEY_RIGHT && Keyboard.getEventKeyState()) {
				moveIndex();
			}
			if (Keyboard.getEventKey() == Keyboard.KEY_S && Keyboard.getEventKeyState()) {
				SaveMap("Map", grid);
			}
		}
	}

	// method that changes the tile type when the mouse is above that tile
	private void setTile() {
		grid.setTile((int) Math.floor(Mouse.getX() / TILE_SIZE),
				(int) Math.floor((HEIGHT - Mouse.getY() - 1) / TILE_SIZE), types[index]);
	}

	// Allow editor to change different tileType
	private void moveIndex() {
		index++;
		if (index > types.length - 1) {
			index = 0;

		}
	}
}
