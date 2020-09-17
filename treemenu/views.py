from django.shortcuts import render
from django.views.generic import TemplateView
from django_pdfkit import PDFView
from .models import MenuItem


class TreeView(TemplateView):
    template_name = 'treemenu/treeview.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rootmenu = MenuItem.objects.filter(parent__isnull=True).first()
        context.update({
            'rootmenu': rootmenu.get_descendants(),
        })
        return context


class TreePDFView(PDFView):
    template_name = 'treemenu/treeview_pdf.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rootmenu = MenuItem.objects.filter(parent__isnull=True).first()
        context.update({
            'rootmenu': rootmenu.get_descendants(),
        })
        return context