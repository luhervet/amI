import { ReactNode } from 'react';

const colorMap: Record<string, string> = {
  // Category
  internal: 'bg-blue-100 text-blue-800',
  external: 'bg-purple-100 text-purple-800',
  partner: 'bg-green-100 text-green-800',
  regulator: 'bg-red-100 text-red-800',
  customer: 'bg-yellow-100 text-yellow-800',
  supplier: 'bg-orange-100 text-orange-800',
  // Influence/interest
  high: 'bg-red-100 text-red-700',
  medium: 'bg-yellow-100 text-yellow-700',
  low: 'bg-green-100 text-green-700',
  // Action status
  pending: 'bg-slate-100 text-slate-700',
  in_progress: 'bg-blue-100 text-blue-700',
  completed: 'bg-green-100 text-green-700',
  cancelled: 'bg-red-100 text-red-700',
  // Priority
  critical: 'bg-red-200 text-red-900',
  // Relation type
  ally: 'bg-green-100 text-green-800',
  neutral: 'bg-slate-100 text-slate-700',
  adversarial: 'bg-red-100 text-red-800',
  reporting: 'bg-blue-100 text-blue-800',
  collaboration: 'bg-purple-100 text-purple-800',
};

export default function Badge({ value, children }: { value?: string; children?: ReactNode }) {
  const key = value || (typeof children === 'string' ? children : '');
  const cls = colorMap[key] || 'bg-slate-100 text-slate-600';
  return (
    <span className={`inline-flex items-center px-2 py-0.5 rounded text-xs font-medium capitalize ${cls}`}>
      {children || value}
    </span>
  );
}
