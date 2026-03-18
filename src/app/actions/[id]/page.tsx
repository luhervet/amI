import ActionForm from '@/components/ActionForm';
import { getAction, getStakeholders } from '@/lib/store';
import { notFound } from 'next/navigation';
import Link from 'next/link';
import Badge from '@/components/Badge';

export const dynamic = 'force-dynamic';

export default async function ActionDetailPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const action = getAction(id);
  if (!action) notFound();

  const stakeholders = getStakeholders();
  const linked = stakeholders.filter((s) => action.stakeholderIds.includes(s.id));

  return (
    <div className="space-y-6 max-w-4xl">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-bold text-slate-900">{action.title}</h2>
          <div className="flex gap-2 mt-1">
            <Badge value={action.status}>{action.status.replace('_', ' ')}</Badge>
            <Badge value={action.priority} />
          </div>
        </div>
        <Link href="/actions" className="text-sm text-slate-600 hover:underline">← Back</Link>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2">
          <ActionForm id={id} stakeholders={stakeholders} initial={{
            title: action.title, description: action.description, stakeholderIds: action.stakeholderIds,
            status: action.status, priority: action.priority, dueDate: action.dueDate,
            owner: action.owner, outcome: action.outcome, tags: action.tags,
          }} />
        </div>

        <div className="space-y-4">
          <div className="bg-white rounded-xl p-4 shadow-sm border border-slate-200">
            <h3 className="font-semibold text-slate-700 mb-3">Details</h3>
            <dl className="space-y-2 text-sm">
              {action.dueDate && <div className="flex justify-between"><dt className="text-slate-500">Due</dt><dd className="text-slate-700">{action.dueDate}</dd></div>}
              {action.owner && <div className="flex justify-between"><dt className="text-slate-500">Owner</dt><dd className="text-slate-700">{action.owner}</dd></div>}
              <div className="flex justify-between"><dt className="text-slate-500">Created</dt><dd className="text-slate-500 text-xs">{new Date(action.createdAt).toLocaleDateString()}</dd></div>
              <div className="flex justify-between"><dt className="text-slate-500">Updated</dt><dd className="text-slate-500 text-xs">{new Date(action.updatedAt).toLocaleDateString()}</dd></div>
            </dl>
            {action.tags.length > 0 && (
              <div className="mt-3 pt-3 border-t border-slate-100 flex flex-wrap gap-1">
                {action.tags.map((t) => (
                  <span key={t} className="bg-slate-100 text-slate-600 text-xs px-2 py-0.5 rounded">{t}</span>
                ))}
              </div>
            )}
          </div>

          {linked.length > 0 && (
            <div className="bg-white rounded-xl p-4 shadow-sm border border-slate-200">
              <h3 className="font-semibold text-slate-700 mb-3">Linked Stakeholders</h3>
              <ul className="space-y-2">
                {linked.map((s) => (
                  <li key={s.id} className="flex items-center gap-2">
                    <div className="w-6 h-6 rounded-full bg-blue-100 flex items-center justify-center text-blue-700 font-bold text-xs flex-shrink-0">
                      {s.name.charAt(0)}
                    </div>
                    <Link href={`/stakeholders/${s.id}`} className="text-sm text-blue-600 hover:underline">{s.name}</Link>
                  </li>
                ))}
              </ul>
            </div>
          )}

          {action.outcome && (
            <div className="bg-white rounded-xl p-4 shadow-sm border border-slate-200">
              <h3 className="font-semibold text-slate-700 mb-2">Outcome</h3>
              <p className="text-sm text-slate-600">{action.outcome}</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
