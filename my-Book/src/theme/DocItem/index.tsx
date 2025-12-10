import React from 'react';
import DocItem from '@theme-original/DocItem';
import type DocItemType from '@theme/DocItem';
import type {WrapperProps} from '@docusaurus/types';
import styles from './styles.module.css';
import clsx from 'clsx';

type Props = WrapperProps<typeof DocItemType>

export default function DocItemWrapper(props: Props): JSX.Element {
  return (
    <div className={clsx(styles.docItemContainer)}>
        <DocItem {...props} />
    </div>
  );
}
