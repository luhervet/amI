import fs from 'fs';
import path from 'path';
import { AppData, Stakeholder, Relation, Action } from './types';

const DATA_FILE = path.join(process.cwd(), 'data', 'app-data.json');

function ensureDataFile(): void {
  const dir = path.dirname(DATA_FILE);
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
  if (!fs.existsSync(DATA_FILE)) {
    const initial: AppData = { stakeholders: [], relations: [], actions: [] };
    fs.writeFileSync(DATA_FILE, JSON.stringify(initial, null, 2));
  }
}

export function readData(): AppData {
  ensureDataFile();
  const raw = fs.readFileSync(DATA_FILE, 'utf-8');
  return JSON.parse(raw) as AppData;
}

export function writeData(data: AppData): void {
  ensureDataFile();
  fs.writeFileSync(DATA_FILE, JSON.stringify(data, null, 2));
}

export function generateId(): string {
  return Date.now().toString(36) + Math.random().toString(36).slice(2, 7);
}

// Stakeholders
export function getStakeholders(): Stakeholder[] {
  return readData().stakeholders;
}

export function getStakeholder(id: string): Stakeholder | undefined {
  return readData().stakeholders.find((s) => s.id === id);
}

export function createStakeholder(data: Omit<Stakeholder, 'id' | 'createdAt' | 'updatedAt'>): Stakeholder {
  const db = readData();
  const now = new Date().toISOString();
  const stakeholder: Stakeholder = { ...data, id: generateId(), createdAt: now, updatedAt: now };
  db.stakeholders.push(stakeholder);
  writeData(db);
  return stakeholder;
}

export function updateStakeholder(id: string, data: Partial<Omit<Stakeholder, 'id' | 'createdAt'>>): Stakeholder | null {
  const db = readData();
  const idx = db.stakeholders.findIndex((s) => s.id === id);
  if (idx === -1) return null;
  db.stakeholders[idx] = { ...db.stakeholders[idx], ...data, updatedAt: new Date().toISOString() };
  writeData(db);
  return db.stakeholders[idx];
}

export function deleteStakeholder(id: string): boolean {
  const db = readData();
  const len = db.stakeholders.length;
  db.stakeholders = db.stakeholders.filter((s) => s.id !== id);
  db.relations = db.relations.filter((r) => r.fromId !== id && r.toId !== id);
  db.actions = db.actions.map((a) => ({ ...a, stakeholderIds: a.stakeholderIds.filter((sid) => sid !== id) }));
  writeData(db);
  return db.stakeholders.length < len;
}

// Relations
export function getRelations(): Relation[] {
  return readData().relations;
}

export function createRelation(data: Omit<Relation, 'id' | 'createdAt' | 'updatedAt'>): Relation {
  const db = readData();
  const now = new Date().toISOString();
  const relation: Relation = { ...data, id: generateId(), createdAt: now, updatedAt: now };
  db.relations.push(relation);
  writeData(db);
  return relation;
}

export function updateRelation(id: string, data: Partial<Omit<Relation, 'id' | 'createdAt'>>): Relation | null {
  const db = readData();
  const idx = db.relations.findIndex((r) => r.id === id);
  if (idx === -1) return null;
  db.relations[idx] = { ...db.relations[idx], ...data, updatedAt: new Date().toISOString() };
  writeData(db);
  return db.relations[idx];
}

export function deleteRelation(id: string): boolean {
  const db = readData();
  const len = db.relations.length;
  db.relations = db.relations.filter((r) => r.id !== id);
  writeData(db);
  return db.relations.length < len;
}

// Actions
export function getActions(): Action[] {
  return readData().actions;
}

export function getAction(id: string): Action | undefined {
  return readData().actions.find((a) => a.id === id);
}

export function createAction(data: Omit<Action, 'id' | 'createdAt' | 'updatedAt'>): Action {
  const db = readData();
  const now = new Date().toISOString();
  const action: Action = { ...data, id: generateId(), createdAt: now, updatedAt: now };
  db.actions.push(action);
  writeData(db);
  return action;
}

export function updateAction(id: string, data: Partial<Omit<Action, 'id' | 'createdAt'>>): Action | null {
  const db = readData();
  const idx = db.actions.findIndex((a) => a.id === id);
  if (idx === -1) return null;
  db.actions[idx] = { ...db.actions[idx], ...data, updatedAt: new Date().toISOString() };
  writeData(db);
  return db.actions[idx];
}

export function deleteAction(id: string): boolean {
  const db = readData();
  const len = db.actions.length;
  db.actions = db.actions.filter((a) => a.id !== id);
  writeData(db);
  return db.actions.length < len;
}
