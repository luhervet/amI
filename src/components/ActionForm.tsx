'use client';

import { useRouter } from 'next/navigation';
import { useState } from 'react';
import { Action, Stakeholder } from '@/lib/types';

type FormData = Omit<Action, 'id' | 'createdAt' | 'updatedAt'>;

const emptyForm: FormData = {
  title: '', description: '', stakeholderIds: [],
  status: 'pending', priority: 'medium',
  dueDate: '', owner: '', outcome: '', tags: [],
};

export default function ActionForm({
  initial, id, stakeholders,
}: {
  initial?: Partial<FormData>;
  id?: string;
  stakeholders: Stakeholder[];
}) {
  const router = useRouter();
  const [form, setForm] = useState<FormData>({ ...emptyForm, ...initial });
  const [tagInput, setTagInput] = useState('');
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState('');

  function set(field: keyof FormData, value: string) {
    setForm((f) => ({ ...f, [field]: value }));
  }

  function toggleStakeholder(sid: string) {
    setForm((f) => ({
      ...f,
      stakeholderIds: f.stakeholderIds.includes(sid)
        ? f.stakeholderIds.filter((x) => x !== sid)
        : [...f.stakeholderIds, sid],
    }));
  }

  function addTag() {
    const t = tagInput.trim();
    if (t && !form.tags.includes(t)) setForm((f) => ({ ...f, tags: [...f.tags, t] }));
    setTagInput('');
  }

  function removeTag(t: string) {
    setForm((f) => ({ ...f, tags: f.tags.filter((x) => x !== t) }));
  }

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setSaving(true);
    setError('');
    try {
      const res = await fetch(id ? `/api/actions/${id}` : '/api/actions', {
        method: id ? 'PATCH' : 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form),
      });
      if (!res.ok) {
        const d = await res.json();
        setError(d.error || 'Save failed');
        return;
      }
      router.push('/actions');
      router.refresh();
    } finally {
      setSaving(false);
    }
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-5 max-w-2xl bg-white rounded-xl p-6 shadow-sm border border-slate-200">
      {error && <p className="text-sm text-red-600 bg-red-50 p-3 rounded-lg">{error}</p>}

      <div>
        <label className="block text-xs font-medium text-slate-600 mb-1">Title *</label>
        <input required value={form.title} onChange={(e) => set('title', e.target.value)}
          className="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500" />
      </div>

      <div>
        <label className="block text-xs font-medium text-slate-600 mb-1">Description</label>
        <textarea rows={3} value={form.description} onChange={(e) => set('description', e.target.value)}
          className="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none" />
      </div>

      <div className="grid grid-cols-2 gap-4">
        <div>
          <label className="block text-xs font-medium text-slate-600 mb-1">Status *</label>
          <select value={form.status} onChange={(e) => set('status', e.target.value)}
            className="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500">
            {['pending', 'in_progress', 'completed', 'cancelled'].map((v) => (
              <option key={v} value={v}>{v.replace('_', ' ')}</option>
            ))}
          </select>
        </div>
        <div>
          <label className="block text-xs font-medium text-slate-600 mb-1">Priority *</label>
          <select value={form.priority} onChange={(e) => set('priority', e.target.value)}
            className="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500">
            {['critical', 'high', 'medium', 'low'].map((v) => (
              <option key={v} value={v}>{v.charAt(0).toUpperCase() + v.slice(1)}</option>
            ))}
          </select>
        </div>
        <div>
          <label className="block text-xs font-medium text-slate-600 mb-1">Due Date</label>
          <input type="date" value={form.dueDate} onChange={(e) => set('dueDate', e.target.value)}
            className="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500" />
        </div>
        <div>
          <label className="block text-xs font-medium text-slate-600 mb-1">Owner</label>
          <input value={form.owner} onChange={(e) => set('owner', e.target.value)}
            className="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500" />
        </div>
      </div>

      <div>
        <label className="block text-xs font-medium text-slate-600 mb-2">Linked Stakeholders</label>
        <div className="border border-slate-200 rounded-lg p-3 max-h-40 overflow-y-auto space-y-1">
          {stakeholders.length === 0 ? (
            <p className="text-xs text-slate-400">No stakeholders available.</p>
          ) : stakeholders.map((s) => (
            <label key={s.id} className="flex items-center gap-2 cursor-pointer hover:bg-slate-50 px-1 py-0.5 rounded">
              <input type="checkbox" checked={form.stakeholderIds.includes(s.id)}
                onChange={() => toggleStakeholder(s.id)} className="rounded" />
              <span className="text-sm text-slate-700">{s.name} <span className="text-slate-400">({s.organization})</span></span>
            </label>
          ))}
        </div>
      </div>

      <div>
        <label className="block text-xs font-medium text-slate-600 mb-1">Outcome / Notes</label>
        <textarea rows={2} value={form.outcome} onChange={(e) => set('outcome', e.target.value)}
          className="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none" />
      </div>

      <div>
        <label className="block text-xs font-medium text-slate-600 mb-1">Tags</label>
        <div className="flex gap-2 mb-2">
          <input value={tagInput} onChange={(e) => setTagInput(e.target.value)}
            onKeyDown={(e) => { if (e.key === 'Enter') { e.preventDefault(); addTag(); } }}
            placeholder="Type and press Enter"
            className="flex-1 border border-slate-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500" />
          <button type="button" onClick={addTag}
            className="text-sm bg-slate-100 hover:bg-slate-200 px-3 py-2 rounded-lg">Add</button>
        </div>
        <div className="flex flex-wrap gap-1">
          {form.tags.map((t) => (
            <span key={t} className="bg-blue-50 text-blue-700 text-xs px-2 py-1 rounded-full flex items-center gap-1">
              {t}
              <button type="button" onClick={() => removeTag(t)} className="hover:text-red-500">×</button>
            </span>
          ))}
        </div>
      </div>

      <div className="flex gap-3 pt-2">
        <button type="submit" disabled={saving}
          className="bg-blue-600 hover:bg-blue-700 text-white text-sm font-medium px-5 py-2 rounded-lg disabled:opacity-50 transition-colors">
          {saving ? 'Saving…' : id ? 'Update Action' : 'Create Action'}
        </button>
        <button type="button" onClick={() => router.back()}
          className="text-sm text-slate-600 hover:text-slate-800 px-4 py-2 rounded-lg border border-slate-300 hover:bg-slate-50">
          Cancel
        </button>
      </div>
    </form>
  );
}
