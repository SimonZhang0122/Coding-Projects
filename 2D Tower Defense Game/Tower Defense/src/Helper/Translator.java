package Helper;

import static org.lwjgl.opengl.GL11.*;

import java.io.IOException;
import java.io.InputStream;

import org.lwjgl.LWJGLException;
import org.lwjgl.opengl.Display;
import org.lwjgl.opengl.DisplayMode;
import org.newdawn.slick.opengl.Texture;
import org.newdawn.slick.opengl.TextureLoader;
import org.newdawn.slick.util.ResourceLoader;

public class Translator {

	public static final int WIDTH = 1344, HEIGHT = 704;// width and height of the whole display screen in tiles
	public static final int TILE_SIZE = 64;// size of each tiles on the map

	public static void BeginSession() {// a method that sets the game screen up
		Display.setTitle("Tower Defense");// the name of the game
		try {
			Display.setDisplayMode(new DisplayMode(1344, 704));// size of the game screen
			Display.create();
		} catch (LWJGLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		glMatrixMode(GL_PROJECTION);
		glLoadIdentity();
		glOrtho(0, WIDTH, HEIGHT, 0, 1, -1);// sets the camera for what the screen will see
		glMatrixMode(GL_MODELVIEW);
		glEnable(GL_TEXTURE_2D);
		glEnable(GL_BLEND);// blends the textures so they can overlap each other
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
	}

	public static boolean CheckCollision(float x1, float y1, float width1, float height1, float x2, float y2,
			float width2, float height2) {
		if (x1 + width1 > x2 && x1 < x2 + width2 && y1 + height1 > y2 && y1 < y2 + height2)// collision check
			return true;
		return false;
	}

	public static void DrawQuad(float x, float y, float width, float height) {// makes a square by drawing lines from
																				// each edge
		glBegin(GL_QUADS);
		glVertex2f(x, y);// top left
		glVertex2f(x + width, y);// top right
		glVertex2f(x + width, y + height);// bottom right
		glVertex2f(x, y + height);// bottom left
		glEnd();
	}

	public static void DrawQuadTex(Texture tex, float x, float y, float width, float height) {// methods that gives
																								// entities and tiles
																								// textures
		tex.bind();// binds textures onto the map and entities
		glTranslatef(x, y, 0);// draws the texture in 2D
		glBegin(GL_QUADS);// begin drawing the square
		glTexCoord2f(0, 0);// top left corner
		glVertex2f(0, 0);// top left vertex
		glTexCoord2f(1, 0);// top right corner
		glVertex2f(width, 0);// top right vertex
		glTexCoord2f(1, 1);// bottom right corner
		glVertex2f(width, height);// bottom right vertex
		glTexCoord2f(0, 1);// bottom left corner
		glVertex2f(0, height);// bottom left vertex
		glEnd();
		glLoadIdentity();// Prevent screen tearing
	}

	public static void DrawQuadTexRot(Texture tex, float x, float y, float width, float height, float angle) {// makes
																												// textures
																												// rotate
		tex.bind();// binds textures onto the map and entities
		glTranslatef(x + width / 2, y + height / 2, 0);// draws the texture in 2D
		glRotatef(angle, 0, 0, 1);// rotates the texture
		glTranslatef(-width / 2, -height / 2, 0);// draws the rotated texture in 2D
		glBegin(GL_QUADS);// begin drawing the square
		glTexCoord2f(0, 0);// top left corner
		glVertex2f(0, 0);// top left vertex
		glTexCoord2f(1, 0);// top right corner
		glVertex2f(width, 0);// top right vertex
		glTexCoord2f(1, 1);// bottom right corner
		glVertex2f(width, height);// bottom right vertex
		glTexCoord2f(0, 1);// bottom left corner
		glVertex2f(0, height);// bottom left vertex
		glEnd();
		glLoadIdentity();// Prevent screen tearing
	}

	public static Texture LoadTexture(String path, String fileType) {// gets textures from resource folder
		Texture tex = null;
		InputStream in = ResourceLoader.getResourceAsStream(path);
		try {
			tex = TextureLoader.getTexture(fileType, in);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return tex;
	}

	public static Texture QuickLoad(String name) {// method that shortens a way to call textures
		Texture tex = null;
		tex = LoadTexture("res/" + name + ".png", "PNG");
		return tex;
	}
}
