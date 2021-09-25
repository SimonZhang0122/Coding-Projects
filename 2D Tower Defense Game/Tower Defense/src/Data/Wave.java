package Data;

import java.util.ArrayList;
import java.util.concurrent.CopyOnWriteArrayList;

import static Helper.Clock.*;
import static Helper.Translator.TILE_SIZE;

public class Wave {// creates and manages a wave of enemy

	private float timeSinceLastSpawn, spawnTime;
	private Enemy enemyType;
	private CopyOnWriteArrayList<Enemy> enemyList;
	private int enemiesPerWave, enemiesSpawned;
	private boolean waveCompleted;

	public Wave(Enemy enemyType, float spawnTime, int enemiesPerWave) {// constructor
		this.enemyType = enemyType;
		this.spawnTime = spawnTime;
		this.enemiesPerWave = enemiesPerWave;
		this.enemiesSpawned = 0;
		this.timeSinceLastSpawn = 0;
		this.enemyList = new CopyOnWriteArrayList<Enemy>();
		this.waveCompleted = false;

		spawn();// spawn a enemy when game first starts
	}

	private void spawn() {// creates new enemies on the map
		enemyList.add(new Enemy(enemyType.getTexture(), enemyType.getStartTile(), enemyType.getTileGrid(), TILE_SIZE,
				TILE_SIZE, enemyType.getSpeed(), enemyType.getHp()));
		enemiesSpawned++;
	}

	public void update() {// keeps spawning the enemy
		boolean allEnemiesDead = true;
		if (enemiesSpawned < enemiesPerWave) {// if the enemies spawned is less than the number of enemies in a wave,
												// keep checking time passed and spawn enemies
			timeSinceLastSpawn += Delta();
			if (timeSinceLastSpawn > spawnTime) {
				spawn();
				timeSinceLastSpawn = 0;
			}
		}
		for (Enemy e : enemyList) {// if all enemies are alive, keep spawning and updating
			if (e.isAlive()) {
				allEnemiesDead = false;
				e.update();
				e.draw();
			} else
				enemyList.remove(e);
		}
		if (allEnemiesDead) // if all enemies are dead, the wave is over
			waveCompleted = true;

	}

	public boolean isCompleted() {
		return waveCompleted;
	}

	public CopyOnWriteArrayList<Enemy> getEnemyList() {
		return enemyList;
	}
}
