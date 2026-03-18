import { getStakeholder, getRelations, getActions, getStakeholders } from '@/lib/store';
import StakeholderForm from '@/components/StakeholderForm';
import Badge from '@/components/Badge';
import Link from 'next/link';
import { notFound } from 'next/navigation';

export const dynamic = 'force-dynamic';

export default async function StakeholderDetailPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const s = getStakeholder(id);
  if (!s) notFound();

  const allRelations = getRelations();
  const allStakeholders = getStakeholders();
  const allActions = getActions();

  const relations = allRelations.filter((r) => r.fromId === id || r.toId === id);
  const actions = allActions.filter((a) => a.stakeholderIds.includes(id));

  function getOther(r: typeof relations[0]) {
    const otherId = r.fromId === id ? r.toId : r.fromId;
    return allStakeholders.find((x) => x.id === otherId);
  }

  return (
    <div className="space-y-6 max-w-4xl">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="w-12 h-12 rounded-full bg-blue-100 flex items-center justify-center text-blue-700 font-bold text-xl">
            {s.name.charAt(0).toUpperCase()}
          </div>
          <div>
            <h2 className="text-2xl font-bold text-slate-900">{s.name}</h2>
            <p className="text-sm text-slate-500">{s.role} at {s.organization}</p>
          </div>
        </div>
        <Link href="/stakeholders" className="text-sm text-slate-600 hover:underline">← Back</Link>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Edit form */}
        <div className="lg:col-span-2">
          <h3 className="font-semibold text-slate-700 mb-3">Profile</h3>
          <StakeholderForm
            id={id}
            initial={{
              name: s.name, organization: s.organization, role: s.role,
              email: s.email, phone: s.phone, category: s.category,
              influence: s.influence, interest: s.interest, notes: s.notes, tags: s.tags,
            }}
          />
        </div>

        {/* Sidebar info */}
        <div className="space-y-4">
          <div className="bg-white rounded-xl p-4 shadow-sm border border-slate-200">
            <h3 className="font-semibold text-slate-700 mb-3">Quick Info</h3>
            <dl className="space-y-2 text-sm">
              <div className="flex justify-between"><dt className="text-slate-500">Category</dt><dd><Badge value={s.category} /></dd></div>
              <div className="flex justify-between"><dt className="text-slate-500">Influence</dt><dd><Badge value={s.influence} /></dd></div>
              <div className="flex justify-between"><dt className="text-slate-500">Interest</dt><dd><Badge value={s.interest} /></dd></div>
              <div className="flex justify-between"><dt className="text-slate-500">Email</dt><dd className="text-right text-xs text-slate-600">{s.email}</dd></div>
              {s.phone && <div className="flex justify-between"><dt className="text-slate-500">Phone</dt><dd className="text-xs text-slate-600">{s.phone}</dd></div>}
            </dl>
            {s.tags.length > 0 && (
              <div className="mt-3 pt-3 border-t border-slate-100">
                <div className="flex flex-wrap gap-1">
                  {s.tags.map((t) => (
                    <span key={t} className="bg-slate-100 text-slate-600 text-xs px-2 py-0.5 rounded">{t}</span>
                  ))}
                </div>
              </div>
            )}
          </div>

          <div className="bg-white rounded-xl p-4 shadow-sm border border-slate-200">
            <h3 className="font-semibold text-slate-700 mb-3">Relations ({relations.length})</h3>
            {relations.length === 0 ? (
              <p className="text-xs text-slate-400">No relations mapped.</p>
            ) : (
              <ul className="space-y-2">
                {relations.map((r) => {
                  const other = getOther(r);
                  return (
                    <li key={r.id} className="text-sm">
                      <span className="text-slate-500">{r.fromId === id ? '→' : '←'} </span>
                      <Link href={`/stakeholders/${other?.id}`} className="text-blue-600 hover:underline">{other?.name || 'Unknown'}</Link>
                      <span className="ml-1"><Badge value={r.type} /></span>
                    </li>
                  );
                })}
              </ul>
            )}
          </div>

          <div className="bg-white rounded-xl p-4 shadow-sm border border-slate-200">
            <h3 className="font-semibold text-slate-700 mb-3">Actions ({actions.length})</h3>
            {actions.length === 0 ? (
              <p className="text-xs text-slate-400">No actions linked.</p>
            ) : (
              <ul className="space-y-2">
                {actions.map((a) => (
                  <li key={a.id} className="text-sm">
                    <p className="font-medium text-slate-800 truncate">{a.title}</p>
                    <Badge value={a.status}>{a.status.replace('_', ' ')}</Badge>
                  </li>
                ))}
              </ul>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
