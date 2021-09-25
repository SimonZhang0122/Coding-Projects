package Helper;

import Data.Editor;
import Data.Game;
import Data.MainMenu;
import Data.TileGrid;

import static Helper.Loader.LoadMap;

public class StateManager {

	public static enum GameState {// a enumerator that is basically a variable
		MAINMENU, GAME, EDITOR
	}

	public static GameState gameState = GameState.MAINMENU;
	public static MainMenu mainMenu;
	public static Game game;
	public static Editor editor;

	static TileGrid map = LoadMap("Map");

	public static void update() {
		switch (gameState) {
		case MAINMENU:
			if (mainMenu == null)
				mainMenu = new MainMenu();
			mainMenu.update();
			break;
		case GAME:
			if (game == null)
				game = new Game(map);
			game.update();
			break;
		case EDITOR:
			if (editor == null)
				editor = new Editor();
			editor.update();
			break;

		}
	}

	public static void setState(GameState newState) {// changes game screens
		gameState = newState;
	}
}
