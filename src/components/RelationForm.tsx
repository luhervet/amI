'use client';

import { useRouter } from 'next/navigation';
import { useState } from 'react';
import { Stakeholder } from '@/lib/types';

export default function RelationForm({ stakeholders }: { stakeholders: Stakeholder[] }) {
  const router = useRouter();
  const [form, setForm] = useState({
    fromId: '', toId: '', type: 'neutral', description: '', strength: 3,
  });
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState('');

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setSaving(true);
    setError('');
    try {
      const res = await fetch('/api/relations', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form),
      });
      if (!res.ok) {
        const d = await res.json();
        setError(d.error || 'Save failed');
        return;
      }
      router.refresh();
      setForm({ fromId: '', toId: '', type: 'neutral', description: '', strength: 3 });
    } finally {
      setSaving(false);
    }
  }

  return (
    <form onSubmit={handleSubmit} className="bg-white rounded-xl p-5 shadow-sm border border-slate-200 space-y-4">
      <h3 className="font-semibold text-slate-800">Add New Relation</h3>
      {error && <p className="text-sm text-red-600 bg-red-50 p-2 rounded">{error}</p>}

      <div className="grid grid-cols-2 gap-3">
        <div>
          <label className="block text-xs font-medium text-slate-600 mb-1">From *</label>
          <select required value={form.fromId} onChange={(e) => setForm((f) => ({ ...f, fromId: e.target.value }))}
            className="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500">
            <option value="">Select stakeholder…</option>
            {stakeholders.map((s) => <option key={s.id} value={s.id}>{s.name} ({s.organization})</option>)}
          </select>
        </div>
        <div>
          <label className="block text-xs font-medium text-slate-600 mb-1">To *</label>
          <select required value={form.toId} onChange={(e) => setForm((f) => ({ ...f, toId: e.target.value }))}
            className="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500">
            <option value="">Select stakeholder…</option>
            {stakeholders.map((s) => <option key={s.id} value={s.id}>{s.name} ({s.organization})</option>)}
          </select>
        </div>
        <div>
          <label className="block text-xs font-medium text-slate-600 mb-1">Relation Type *</label>
          <select value={form.type} onChange={(e) => setForm((f) => ({ ...f, type: e.target.value }))}
            className="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500">
            {['ally', 'neutral', 'adversarial', 'reporting', 'collaboration'].map((v) => (
              <option key={v} value={v}>{v.charAt(0).toUpperCase() + v.slice(1)}</option>
            ))}
          </select>
        </div>
        <div>
          <label className="block text-xs font-medium text-slate-600 mb-1">Strength (1–5) *</label>
          <input type="number" min={1} max={5} value={form.strength}
            onChange={(e) => setForm((f) => ({ ...f, strength: parseInt(e.target.value) }))}
            className="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500" />
        </div>
      </div>

      <div>
        <label className="block text-xs font-medium text-slate-600 mb-1">Description</label>
        <input value={form.description} onChange={(e) => setForm((f) => ({ ...f, description: e.target.value }))}
          className="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500" />
      </div>

      <button type="submit" disabled={saving}
        className="bg-blue-600 hover:bg-blue-700 text-white text-sm font-medium px-5 py-2 rounded-lg disabled:opacity-50 transition-colors">
        {saving ? 'Adding…' : 'Add Relation'}
      </button>
    </form>
  );
}
