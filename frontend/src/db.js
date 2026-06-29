import Dexie from 'dexie';

export const db = new Dexie('WranglerBD');
db.version(1).stores({
    itineraries: '++id, city, timestamp',
    sosData: 'city'
});

export async function saveItinerary(city, payload) {
    await db.itineraries.add({
        city,
        payload,
        timestamp: new Date().toDateString()
    });
}