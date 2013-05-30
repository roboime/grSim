/*
grSim - RoboCup Small Size Soccer Robots Simulator
Copyright (C) 2011, Parsian Robotic Center (eew.aut.ac.ir/~parsian/grsim)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

#include "statuswidget.h"
#include <QSizePolicy>
#define INITIAL_HEIGHT 75

class CustomText : public QTextEdit
{
public:
    CustomText(QWidget *parent) : QTextEdit(parent) {}
    QSize sizeHint() const { return QSize(600, INITIAL_HEIGHT); }
};

CStatusWidget::CStatusWidget(CStatusPrinter* _statusPrinter)
{
    statusPrinter = _statusPrinter;
    logTime.start();

    this->setAllowedAreas(Qt::BottomDockWidgetArea);
    this->setFeatures(QDockWidget::NoDockWidgetFeatures);

    //statusText = new QTextEdit(this);
    statusText = new CustomText(this);
    statusText->setReadOnly(true);
    titleLbl = new QLabel(tr("Messages"));

    this->setWidget(statusText);
    this->setTitleBarWidget(titleLbl);

    // XXX fix initial size
    statusText->setSizePolicy(QSizePolicy(QSizePolicy::Preferred, QSizePolicy::Minimum));
    //this->setSizePolicy(QSizePolicy(QSizePolicy::Fixed, QSizePolicy::Minimum));
}

void CStatusWidget::write(QString str, QColor color)
{
    if( statusText->textCursor().blockNumber() > 2000 )
        statusText->clear();

    statusText->setTextColor(color);
    //statusText->append(QString::number(statusText->textCursor().blockNumber()) + " : " + str);
    //statusText->append(QString::number(logTime.elapsed()) + " : " + str);
    statusText->append(str);

    statusText->setTextColor(QColor("black"));
}

void CStatusWidget::update()
{
    CStatusText text;
    while(!statusPrinter->textBuffer.isEmpty())
    {
        text = statusPrinter->textBuffer.dequeue();
        write(text.text, text.color);
    }
}

