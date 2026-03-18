export type StakeholderCategory = 'internal' | 'external' | 'partner' | 'regulator' | 'customer' | 'supplier';
export type StakeholderInfluence = 'high' | 'medium' | 'low';
export type RelationType = 'ally' | 'neutral' | 'adversarial' | 'reporting' | 'collaboration';
export type ActionStatus = 'pending' | 'in_progress' | 'completed' | 'cancelled';
export type ActionPriority = 'critical' | 'high' | 'medium' | 'low';

export interface Stakeholder {
  id: string;
  name: string;
  organization: string;
  role: string;
  email: string;
  phone?: string;
  category: StakeholderCategory;
  influence: StakeholderInfluence;
  interest: StakeholderInfluence;
  notes?: string;
  tags: string[];
  createdAt: string;
  updatedAt: string;
}

export interface Relation {
  id: string;
  fromId: string;
  toId: string;
  type: RelationType;
  description?: string;
  strength: number; // 1-5
  createdAt: string;
  updatedAt: string;
}

export interface Action {
  id: string;
  title: string;
  description?: string;
  stakeholderIds: string[];
  status: ActionStatus;
  priority: ActionPriority;
  dueDate?: string;
  owner?: string;
  outcome?: string;
  tags: string[];
  createdAt: string;
  updatedAt: string;
}

export interface AppData {
  stakeholders: Stakeholder[];
  relations: Relation[];
  actions: Action[];
}
